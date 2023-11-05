from datetime import datetime

import bcrypt
from elasticsearch_dsl import Search, Q, A
from elasticsearch_dsl.query import MultiMatch, EMPTY_QUERY
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Query, Mapper
from sqlalchemy.sql import expression

from models.id_worker import IdWorker
from utilities.constant import QUERY_SEPARATE_SYMBOL, CONDITION_SEPARATE_SYMBOL, VALUE_SEPARATE_SYMBOL, \
    HOURS_SEPARATE_SYMBOL, FULLTEXT_SEARCH_BIG_NUMBER, machine_id, ORDER_SEPARATE_SYMBOL, DIRECTION_SEPARATE_SYMBOL, \
    PASSWORD_ENCODING
from utilities.exception import EntityNotFoundException, BadRequestException
from utilities.helper import Utility


class Base(Model):
    def __repr__(self):
        return '<{} with {}>'.format(self.__tablename__, self.id)

    def update(self, value):
        for k, v in value.items():
            if k != 'id':
                setattr(self, k, v)


class BaseQuery(Query):
    def _get_models(self, query):
        if hasattr(query, 'attr'):
            return query.attr.target_mapper
        else:
            return Utility.first_or_none(
                [d['expr'].class_ for d in query.column_descriptions if isinstance(d['expr'], Mapper)])

    def active(self):
        model_class = self._get_models(self)
        if model_class:
            if hasattr(model_class, 'is_active'):
                return self.filter(model_class.is_active == expression.true())

        return self

    def not_deleted(self):
        model_class = self._get_models(self)
        if model_class:
            if hasattr(model_class, 'is_deleted'):
                return self.filter(model_class.is_deleted == expression.false())

        return self

    def get_or_404(self, id_, include_soft_delete=False, include_inactive=False):
        entity = self.get(id_)
        not_found = False
        model_class = self._get_models(self)

        if not entity:
            not_found = True

        if not not_found and not include_soft_delete and hasattr(model_class, 'is_deleted'):
            not_found = entity.is_deleted == True

        if not not_found and not include_inactive and hasattr(model_class, 'is_active'):
            not_found = entity.is_active == False

        if not_found:
            raise EntityNotFoundException(id_, model_class.__tablename__)

        return entity

    def get_by_ids(self, ids: list):
        model_class = self._get_models(self)
        if model_class and ids:
            return self.active().filter(
                model_class.is_active,
                model_class.id.in_(ids)
            )

        return self


db = SQLAlchemy(model_class=Base, query_class=BaseQuery)
id_handler = IdWorker(machine_id())


class IdMixin(object):
    id = db.Column(db.Integer, primary_key=True)


class DistributeIdMixin(object):
    id = db.Column(db.BigInteger, primary_key=True)

    def __init__(self, **kwargs):
        self.id = kwargs.pop('id', id_handler.next_id())


class MultiTenantMixin(object):
    @declared_attr
    def tenant_id(cls):
        return db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=True)


class CreationTimeMixin(object):
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)


class ModificationTimeMixin(object):
    modification_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SlugableMixin(object):
    slug = db.Column(db.String(256), unique=True, nullable=False)

    @classmethod
    def get_by_slug_or_none(cls, slug):
        if not slug:
            return None

        return cls.query.filter(cls.slug == slug).first()

    @classmethod
    def get_by_slug_or_404(cls, slug):
        entity = None

        if slug:
            entity = cls.query.filter(cls.slug == slug).first()

        if entity is None:
            raise EntityNotFoundException(slug, cls.__tablename__)

        return entity


class PassivableMixin(object):
    is_active = db.Column(db.Boolean, unique=False, default=True, server_default=expression.true())


class SoftDeleteMixin(object):
    is_deleted = db.Column(db.Boolean, unique=False, default=False, server_default=expression.false())


class SuspendMixin(object):
    is_suspended = db.Column(db.Boolean, unique=False, default=False, server_default=expression.false())


class ModificationUserMixin(object):
    updated_by = db.Column(db.Integer)


class CreationUserMixin(object):
    created_by = db.Column(db.Integer)


class PublishableMixin(object):
    publish_to_search = db.Column(db.Boolean, unique=False, default=True, server_default=expression.true())


class UserMixin(object):
    email = db.Column(db.String(50), unique=True)
    _password = db.Column('password', db.String(128))
    full_name = db.Column(db.String(128))
    phone_number = db.Column(db.String(20))
    avatar = db.Column(db.String(256))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')

    def verify_password(self, password):
        if self.password is None:
            return False

        return bcrypt.checkpw(password.encode(PASSWORD_ENCODING), self.password.encode(PASSWORD_ENCODING))


class SearchableMixin(object):
    __searchable__ = True
    __mappings__ = {}
    __tablename__ = ''
    __nested__ = []
    __terms__ = []
    __ids__ = []
    __range__ = []
    __geo_distance__ = []
    __term_aggregation__ = ''
    __term_aggregation_enum__ = None

    @classmethod
    def get_response_(cls, client, expression_, from_=0, size=FULLTEXT_SEARCH_BIG_NUMBER, fields=[], order_by=[]):
        s = Search(using=client, index=cls.__tablename__)

        if cls.__term_aggregation__ and cls.__term_aggregation_enum__:
            for agg_enum in cls.__term_aggregation_enum__:
                field_name = agg_enum.name.lower()
                agg = A('terms', field='{}.{}'.format(cls.__term_aggregation__, field_name))
                s.aggs.bucket(field_name, agg)

        s = s.query(expression_)

        if len(order_by):
            s = s.sort(*order_by)
        else:
            s = s.sort()

        if len(fields):
            s = s.source(fields)

        s = s[from_:size]

        return s.execute()

    @classmethod
    def search_(cls, client, expression_, from_=0, size=FULLTEXT_SEARCH_BIG_NUMBER, fields=[], order_by=[]):
        rv = []
        total = 0

        response = cls.get_response_(client, expression_, from_, size, fields, order_by)
        if response.success():
            total = response.hits.total
            rv = response.hits

            if len(fields) == 1:
                field = fields[0]
                rv = [item[field] for item in rv]

        return total, rv

    @classmethod
    def search(cls, client, expression_, offset=0, limit=FULLTEXT_SEARCH_BIG_NUMBER, fields: list = [], order_by=[]):
        q = cls._query_parser(expression_)
        return cls.search_(client, q, offset, limit + offset, fields, order_by)

    @classmethod
    def aggregation_search_(cls, client, expression_, from_=0, size=FULLTEXT_SEARCH_BIG_NUMBER, fields=[], order_by=[]):
        rv = dict(total=0, items=[], aggregations={})

        response = cls.get_response_(client, expression_, from_, size, fields, order_by)
        if response.success():
            rv['total'] = response.hits.total
            rv['items'] = response.hits
            rv['aggregations'] = cls._aggregation_parser(response.aggregations)

            if len(fields) == 1:
                field = fields[0]
                rv['items'] = [item[field] for item in rv['items']]

        return rv

    @classmethod
    def aggregation_search(cls, client, expression_, offset=0, limit=FULLTEXT_SEARCH_BIG_NUMBER, fields: list = [],
                           order_by=[]):
        q = cls._query_parser(expression_)
        return cls.aggregation_search_(client, q, offset, limit + offset, fields, order_by)

    @classmethod
    def _query_parser(cls, expression_: str):
        [free_text, *conditions] = expression_.split(QUERY_SEPARATE_SYMBOL)

        if free_text:
            q = cls._get_free_text_search_query(free_text)
        else:
            q = EMPTY_QUERY

        for condition in conditions:
            if not condition:
                continue

            [field, values] = condition.split(CONDITION_SEPARATE_SYMBOL)
            values = values.split(VALUE_SEPARATE_SYMBOL)

            if field in cls.__terms__:
                q = q & cls._terms_query_parser(field, values)
            elif field in cls.__nested__:
                q = q & cls._nested_query_parser(field, values)
            elif field in cls.__ids__:
                q = q & cls._ids_query_parser(values)
            elif field in cls.__range__:
                values = values[0] if len(values) > 0 else ''
                [gte, lte] = values.split(HOURS_SEPARATE_SYMBOL) if HOURS_SEPARATE_SYMBOL in values else [values, '']
                q = q & cls._range_query_parser(field, gte, lte)
            elif field in cls.__geo_distance__:
                q = q & cls._geo_query_parser(field, values)
        return q

    @classmethod
    def _get_free_text_search_query(cls, free_text: str):
        return MultiMatch(query=free_text, type='phrase')

    @classmethod
    def _nested_query_parser(cls, field, values):
        return Q('nested', path=field, query=Q('terms', **{'{}.id'.format(field): values}))

    @classmethod
    def _ids_query_parser(cls, values):
        return Q('ids', values=values)

    @classmethod
    def _range_query_parser(cls, field, gte, lte):
        return Q('range', **{field: {
            'gte': gte,
            'lte': lte,
            'format': 'strict_hour_minute'
        }})

    @classmethod
    def _terms_query_parser(cls, field, values):
        return Q('terms', **{field: values})

    @classmethod
    def _geo_query_parser(cls, field, values):
        [lat, lon, distance] = values
        return Q('geo_distance', distance='{}km'.format(distance), **{field: {'lat': lat, 'lon': lon}})

    @classmethod
    def _aggregation_parser(cls, aggregations):
        result = []
        for agg_enum in cls.__term_aggregation_enum__:
            field_name = agg_enum.name.lower()
            buckets = []
            for agg in list(aggregations[field_name].buckets):
                buckets.append({
                    'id': agg.key,
                    'count': agg.doc_count,
                })

            result.append({
                'name': field_name,
                'type': agg_enum.value,
                'buckets': buckets,
            })

        return result


class SortableMixin(object):
    __sql_order_fields__ = []
    __distance_order_fields__ = []
    __i18n_order_fields__ = []
    __number_order_fields__ = []
    __keyword_order_fields__ = []

    __descending_symbol = 'desc'
    __ascending_symbol = 'asc'

    @classmethod
    def order_by_sql(cls, query: any, expression_=''):
        if expression_ == '':
            return query.order_by(None)

        conditions = expression_.split(ORDER_SEPARATE_SYMBOL)
        conditions = [c for c in conditions if c in cls.__sql_order_fields__]
        for c in conditions:
            direction = cls.__ascending_symbol
            key = c

            if DIRECTION_SEPARATE_SYMBOL in c:
                key, direction = c.split(DIRECTION_SEPARATE_SYMBOL)

            if direction == cls.__descending_symbol:
                query = query.order_by(getattr(cls, key).desc())
            elif direction == cls.__ascending_symbol:
                query = query.order_by(getattr(cls, key).asc())
            else:
                raise BadRequestException(
                    detail='Invalid direction value at field {}. Only accept "{}" for ascending or "{}" for '
                    'descending'.format(c, cls.__ascending_symbol, cls.__ascending_symbol)
                )

        return query

    @classmethod
    def parse_to_order_document_query(cls, expression_=''):
        rv = []

        if expression_ == '':
            return rv

        conditions = expression_.split(ORDER_SEPARATE_SYMBOL)

        for c in conditions:
            direction = cls.__ascending_symbol
            key = c
            value = ''

            if CONDITION_SEPARATE_SYMBOL in c:
                key, value = c.split(CONDITION_SEPARATE_SYMBOL)

            if DIRECTION_SEPARATE_SYMBOL in key:
                key, direction = key.split(DIRECTION_SEPARATE_SYMBOL)

            if direction != cls.__descending_symbol and direction != cls.__ascending_symbol:
                raise BadRequestException(
                    detail='Invalid order symbol at field {}. Only accept "{}" for ascending or "{}" for '
                    'descending'.format(c, cls.__ascending_symbol, cls.__descending_symbol)
                )

            if key in cls.__distance_order_fields__:
                if value == '':
                    raise BadRequestException(detail='Must specific a coordinate in order by distance field.')

                lat, long = value.split(VALUE_SEPARATE_SYMBOL)
                rv.append({
                    '_geo_distance': {
                        key: {
                            'lat': lat,
                            'lon': long
                        },
                        'order': direction,
                        'unit': 'km',
                        'distance_type': 'arc'
                    }
                })
            elif key in cls.__i18n_order_fields__:
                if value == '':
                    raise BadRequestException(detail='Must specific a locale in order by i18n field.')

                rv.append({
                    '{}.display_text'.format(key): {
                        'order': direction,
                        'nested': {
                            'path': key,
                            'filter': {
                                'term': { '{}.locale_id'.format(key): value}
                            }
                        }
                    }
                })
            elif key in cls.__number_order_fields__:
                rv.append({'{}'.format(key): {'order': direction}})
            elif key in cls.__keyword_order_fields__:
                rv.append('{}{}.keyword'.format('' if direction == cls.__ascending_symbol else '-', key))

        return rv


