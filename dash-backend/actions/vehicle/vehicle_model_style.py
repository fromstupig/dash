from flask import request

from actions.vehicle.vehicle_gallery_item import vehicle_gallery_item_action
from models import db
from models.vehicle import VehicleAttributeValue, VehicleOptionItem, VehicleYearModel
from models.vehicle.vehicle_model_style import VehicleModelStyle
from models.vehicle.vehicle_gallery_item import VehicleGalleryItemType
from schemas.vehicle.vehicle_attribute_value import vehicle_attribute_values_schema
from schemas.vehicle.vehicle_model_style import vehicle_model_style_schema, vehicle_model_styles_schema
from schemas.vehicle.vehicle_option_item import vehicle_option_items_schema
from services.search import SearchService
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class VehicleModelStyleAction:
    def create(self, data):
        validated_data = vehicle_model_style_schema.load(data)
        entity = VehicleModelStyle(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return vehicle_model_style_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleModelStyle.query if q == '' else VehicleModelStyle.query.filter(
            VehicleModelStyle.name.like('%{}%'.format(q)))
        query = query.filter(VehicleModelStyle.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleModelStyle.name.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleModelStyle.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_model_styles_schema.dump(items)

        return rv, total

    def get_all_model_styles_by_vehicle_year_model_id(self, vehicle_year_model_id, sort, direction, limit, offset,
                                                      is_active, q=''):
        current_vehicle_year_model = VehicleYearModel.query.get(vehicle_year_model_id)
        if not current_vehicle_year_model:
            raise EntityNotFoundException(vehicle_year_model_id, 'VehicleYearModel')

        query = VehicleModelStyle.query if q == '' else VehicleModelStyle.query.filter(
            VehicleModelStyle.name.like('%{}%'.format(q)))
        query = query.filter(VehicleModelStyle.is_active == is_active) if is_active is not None else query
        query = query.filter(
            VehicleModelStyle.vehicle_year_model_id == vehicle_year_model_id) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleModelStyle.name.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleModelStyle.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_model_styles_schema.dump(items)

        return rv, total

    def get(self, id_):
        current_vehicle_model_style = VehicleModelStyle.query.get(id_)
        if not current_vehicle_model_style:
            raise EntityNotFoundException(id_, 'VehicleModelStyle')

        return vehicle_model_style_schema.dump(current_vehicle_model_style)

    def update(self, id_, data):
        current_vehicle_model_style = VehicleModelStyle.query.get(id_)
        if not current_vehicle_model_style:
            raise EntityNotFoundException(id_, 'VehicleModelStyle')

        validated_data = vehicle_model_style_schema.load(data)
        validated_data['id'] = None
        current_vehicle_model_style.update(validated_data)
        db.session.commit()

        return vehicle_model_style_schema.dump(current_vehicle_model_style)

    def update_avatar(self, id_, files):

        current_vehicle_model_style = VehicleModelStyle.query.get(id_)
        if not current_vehicle_model_style:
            raise EntityNotFoundException(id_, 'VehicleModelStyle')

        current_vehicle_model_style._galleries = list(
            filter(lambda g: g.type is not VehicleGalleryItemType.MODEL_STYLE_AVATAR,
                   current_vehicle_model_style._galleries))

        current_vehicle_model_style._galleries.extend(vehicle_gallery_item_action. \
                                                      create_gallery_items(VehicleGalleryItemType.MODEL_STYLE_AVATAR,
                                                                           files))

        db.session.commit()

        return vehicle_model_style_schema.dump(current_vehicle_model_style)

    def update_cover(self, id_, files):

        current_vehicle_model_style = VehicleModelStyle.query.get(id_)
        if not current_vehicle_model_style:
            raise EntityNotFoundException(id_, 'VehicleModelStyle')

        current_vehicle_model_style._galleries = list(
            filter(lambda g: g.type is not VehicleGalleryItemType.COVER,
                   current_vehicle_model_style._galleries))

        current_vehicle_model_style._galleries.extend(vehicle_gallery_item_action. \
                                                      create_gallery_items(VehicleGalleryItemType.COVER,
                                                                           files))

        db.session.commit()

        return vehicle_model_style_schema.dump(current_vehicle_model_style)

    def update_introduction_video(self, id_, files):

        current_vehicle_model_style = VehicleModelStyle.query.get(id_)
        if not current_vehicle_model_style:
            raise EntityNotFoundException(id_, 'VehicleModelStyle')

        current_vehicle_model_style._galleries = list(
            filter(lambda g: g.type is not VehicleGalleryItemType.VIDEO_INTRODUCTION,
                   current_vehicle_model_style._galleries))

        current_vehicle_model_style._galleries.extend(vehicle_gallery_item_action. \
                                                      create_gallery_items(VehicleGalleryItemType.VIDEO_INTRODUCTION,
                                                                           files))

        db.session.commit()

        return vehicle_model_style_schema.dump(current_vehicle_model_style)

    def delete(self, id_):
        vehicle_model_style = VehicleModelStyle.query.get(id_)
        if not vehicle_model_style:
            raise EntityNotFoundException(id_, 'VehicleModelStyle')

        db.session.delete(vehicle_model_style)
        db.session.commit()

    def update_attribute_values(self, id_, data, is_override=False):
        vehicle_model_style = VehicleModelStyle.query.get(id_)
        if not vehicle_model_style:
            raise EntityNotFoundException(id_, 'VehicleModelStyle')

        if is_override:
            vehicle_model_style.attributes = []

        d_vehicle_attribute_values = vehicle_attribute_values_schema.load(data)
        for d_vehicle_attribute_value in d_vehicle_attribute_values:
            vehicle_attribute_value = VehicleAttributeValue(**d_vehicle_attribute_value)
            vehicle_model_style.attributes.append(vehicle_attribute_value)
        db.session.commit()

        return vehicle_model_style_schema.dump(vehicle_model_style)

    def update_options(self, id_, data, is_override=False):
        vehicle_model_style = VehicleModelStyle.query.get(id_)
        if not vehicle_model_style:
            raise EntityNotFoundException(id_, 'VehicleModelStyle')

        if is_override:
            vehicle_model_style.options = []

        d_vehicle_options = vehicle_option_items_schema.load(data)
        for d_vehicle_option in d_vehicle_options:
            vehicle_option_item = VehicleOptionItem(**d_vehicle_option)
            vehicle_model_style.options.append(vehicle_option_item)
        db.session.commit()

        return vehicle_model_style_schema.dump(vehicle_model_style)

    def search(self, model_style_search_params):
        search_service = SearchService()
        result = search_service.search_model_styles(model_style_search_params)

        return result


vehicle_model_style_action = VehicleModelStyleAction()
