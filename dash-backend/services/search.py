import json

from elasticsearch_dsl import Search, UpdateByQuery, Q
from flask import current_app

from schemas.vehicle.vehicle import els_vehicle_schema
from schemas.vehicle.vehicle_model_style import els_vehicle_model_style_schema
from utilities.constant import FULLTEXT_SEARCH_BIG_NUMBER, DEFAULT_LANGUAGE
from utilities.helper import Utility

schema = {
    'vehicle_model_styles': els_vehicle_model_style_schema,
    'vehicles': els_vehicle_schema
}


def index_to_search(index, doc_type, model):
    # TODO: Move index step to background jobs
    es = current_app.elastic_search
    if not es.indices.exists(index):
        settings = model.__mappings__
        es.indices.create(index=index, body=settings)

    payload = schema[index].dump(model)
    current_app.elastic_search.index(index=index, doc_type=doc_type, id=model.id, body=payload)


def remove_from_index(index, doc_type, model):
    current_app.elastic_search.delete(index=index, doc_type=doc_type, id=model.id, ignore=404)


def suggest_parser(prefix, suggest_field):
    # TODO: must construct sort field more dynamic instead of hard code
    rv = {
        'query': {
            'match': {
            }
        },
        'sort': [{'slug': {'order': 'asc'}}],
        'from': 0, 'size': FULLTEXT_SEARCH_BIG_NUMBER
    }

    rv['query']['match'][suggest_field] = {
        'query': prefix,
        'operator': 'and'
    }

    return rv


def suggest_completion(indices, prefix, suggest_field, display_language=DEFAULT_LANGUAGE):
    indices_string = ','.join(indices)

    if not current_app.elastic_search:
        return []

    suggest_body = suggest_parser(prefix, suggest_field)
    search = current_app.elastic_search.search(index=indices_string, body=suggest_body)

    rv = {index: [] for index in indices}
    for hit in search['hits']['hits']:
        if hit['_index'] not in rv:
            rv[hit['_index']] = []

        value = hit['_source']

        value['text'] = ''
        for text in value['_texts']:
            if text['locale_id'] == display_language:
                value['text'] = text['display_text']

        del value[suggest_field]
        del value['_texts']
        rv[hit['_index']].append(value)

    return rv


def remove_index(index):
    current_app.elastic_search.indices.delete(index=index, ignore=[400, 404])


def reindex(model):
    for obj in model.query.active().not_deleted().all():
        if obj.vehicle_model_style.technical_feature is not None:
            str_technical_feature = json.dumps(obj.vehicle_model_style.technical_feature)
            obj.vehicle_model_style.technical_feature = str_technical_feature
            # if "Trans Description Cont." in obj.vehicle_model_style.technical_feature['Transmission']:
            #     del obj.vehicle_model_style.technical_feature['Transmission']["Trans Description Cont."]
        if obj.vehicle_model_style.standard_feature is not None:
            str_standard_feature = json.dumps(obj.vehicle_model_style.standard_feature)
            obj.vehicle_model_style.standard_feature = str_standard_feature

        if obj.vehicle_model_style.consumer_info is not None:
            str_consumer_info = json.dumps(obj.vehicle_model_style.consumer_info)
            obj.vehicle_model_style.consumer_info = str_consumer_info

        if obj.vehicle_model_style.pricing_options is not None:
            str_pricing_options = json.dumps(obj.vehicle_model_style.pricing_options)
            obj.vehicle_model_style.pricing_options = str_pricing_options
        print(obj.vehicle_model_style.consumer_info)
        index_to_search(obj.__tablename__, obj.__tablename__, obj)


def before_commit(session):
    session.changes_ = {
        'add': list(session.new),
        'update': list(session.dirty),
        'delete': list(session.deleted)
    }


def after_commit(session):
    for obj in session.changes_['add']:
        need_index = _is_document(obj) and _need_index(obj)

        if not need_index:
            continue

        index_to_search(obj.__tablename__, obj.__tablename__, obj)

    for obj in session.changes_['update']:
        if not _is_document(obj):
            continue

        need_remove = not _need_index(obj)

        if need_remove:
            remove_from_index(obj.__tablename__, obj.__tablename__, obj)
        else:
            index_to_search(obj.__tablename__, obj.__tablename__, obj)

    for obj in session.changes_['delete']:
        if not _is_document(obj):
            continue

        remove_from_index(obj.__tablename__, obj.__tablename__, obj)

    session.changes_ = None


def _is_document(obj: any) -> bool:
    return hasattr(obj, '__searchable__') and obj.__searchable__


def _need_index(obj: any) -> bool:
    rv = True

    if hasattr(obj, 'is_active') or hasattr(obj, 'is_deleted'):
        rv = Utility.get_attribute(obj, 'is_active') or Utility.get_attribute(obj, 'is_deleted')

    if hasattr(obj, 'publish_to_search'):
        rv = rv & Utility.get_attribute(obj, 'publish_to_search')

    return rv


class SearchService:
    def __init__(self):
        self._cached_template = {}
        self.client = current_app.elastic_search

    def search_model_styles(self, search_params):
        if 'filter_search' in search_params and search_params['filter_search'] != '':
            mlt_query = Q("multi_match", query=search_params['filter_search'], fields=['name', 'description'])
        else:
            mlt_query = Q("match_all")

        if 'filter_brand_id' in search_params and search_params['filter_brand_id'] != '':
            brand_match_query = Q("multi_match", query=search_params['filter_brand_id'],
                                  fields=['vehicle_year_model.vehicle_model.vehicle_brand.id'])
        else:
            brand_match_query = Q("match_all")

        if 'filter_model_id' in search_params and search_params['filter_model_id'] != '':
            model_match_query = Q("multi_match", query=search_params['filter_model_id'],
                                  fields=['vehicle_year_model.vehicle_model.id'])
        else:
            model_match_query = Q("match_all")

        if 'filter_year_model_id' in search_params and search_params['filter_year_model_id'] != '':
            year_model_match_query = Q("multi_match", query=search_params['filter_year_model_id'],
                                       fields=['vehicle_year_model.id'])
        else:
            year_model_match_query = Q("match_all")

        if 'filter_body_id' in search_params and search_params['filter_body_id'] != '':
            body_match_query = Q("multi_match", query=search_params['filter_body_id'],
                                 fields=['body.id'])
        else:
            body_match_query = Q("match_all")

        function_query = mlt_query & brand_match_query & model_match_query \
                         & year_model_match_query \
                         & body_match_query

        s = Search(using=current_app.elastic_search).index('vehicle_model_styles').query(function_query)
        s.sort({'_score': {'order': 'desc'}})
        if 'filter_offset' in search_params and "filter_limit" in search_params:
            s = s[search_params['filter_offset']:search_params['filter_offset'] + search_params['filter_limit']]
        response = s.execute()
        h = response['hits']['hits']
        result = []
        if len(h) > 0:
            for item in h:
                result.append(item["_source"].to_dict())

        return result

    def search_vehicle(self, search_params):
        if 'filter_search' in search_params and search_params['filter_search'] != '':
            mlt_query = Q("multi_match", query=search_params['filter_search'],
                          fields=['vehicle_model_style.name', 'vehicle_model_style.description',
                                  'vehicle_model_style.vehicle_year_model.name'
                                  'vehicle_brand.name', 'vehicle_model.description'])
        else:
            mlt_query = Q("match_all")

        if 'filter_brand_id' in search_params and search_params['filter_brand_id'] != '':
            brand_match_query = Q("term", vehicle_brand_id=search_params['filter_brand_id'])
        else:
            brand_match_query = Q("match_all")

        if 'filter_model_id' in search_params and search_params['filter_model_id'] != '':
            model_match_query = Q("term", vehicle_model_id=search_params['filter_model_id'])
        else:
            model_match_query = Q("match_all")

        if 'filter_year_model_id' in search_params and search_params['filter_year_model_id'] != '':
            year_model_match_query = Q("term",
                                       vehicle_model_style__vehicle_year_model_id=search_params['filter_year_model_id'])
        else:
            year_model_match_query = Q("match_all")

        if 'filter_model_style_id' in search_params and search_params['filter_model_style_id'] != '':
            model_style_match_query = Q("term", vehicle_model_style_id=search_params['filter_model_style_id'])
        else:
            model_style_match_query = Q("match_all")

        if 'filter_model_style_color_code' in search_params and search_params['filter_model_style_color_code'] != '':
            model_style_color_match_query = Q("nested", path='custom_options', query=Q("multi_match",
                                                                                       query=search_params[
                                                                                           'filter_model_style_color_code'],
                                                                                       fields=[
                                                                                           'custom_options.detail.code']))
        else:
            model_style_color_match_query = Q("match_all")

        if 'filter_body_id' in search_params and search_params['filter_body_id'] != '':
            body_match_query = Q("term", vehicle_model_style__body_id=search_params['filter_body_id'])
        else:
            body_match_query = Q("match_all")

        if 'filter_price_from' in search_params and search_params['filter_price_from'] != '':
            if 'filter_price_to' in search_params and search_params['filter_price_to'] != '':
                price_range_match_query = Q("range",
                                            vehicle_model_style__base_MSRP={'gte': search_params['filter_price_from'],
                                                                            'lte': search_params['filter_price_to']})
            else:
                price_range_match_query = Q("range",
                                            vehicle_model_style__base_MSRP={'gte': search_params['filter_price_from']})
        else:
            price_range_match_query = Q("match_all")

        function_query = mlt_query & brand_match_query & model_match_query \
                         & year_model_match_query \
                         & body_match_query & model_style_match_query & price_range_match_query \
                         & model_style_color_match_query

        s = Search(using=current_app.elastic_search).index('vehicles').query(function_query)
        s.sort({'_score': {'order': 'desc'}})
        if 'filter_offset' in search_params and "filter_limit" in search_params:
            s = s[search_params['filter_offset']:search_params['filter_limit']]
        s = s.source(excludes=["vehicle_model_style.options", "vehicle_model_style.standard_feature",
                               "vehicle_model_style.pricing_options", "vehicle_model_style.technical_feature",
                               "vehicle_model_style.consumer_info"])
        response = s.execute()
        h = response['hits']['hits']
        total = response['hits']['total']
        result = []
        if len(h) > 0:
            for item in h:
                result.append(item["_source"].to_dict())

        return result, total
