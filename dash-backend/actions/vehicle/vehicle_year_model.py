from flask import request

from actions.vehicle.vehicle_gallery_item import vehicle_gallery_item_action
from models import db
from models.vehicle import VehicleAttributeValue, VehicleModel
from models.vehicle.vehicle_year_model import VehicleYearModel
from models.vehicle.vehicle_gallery_item import VehicleGalleryItemType
from schemas.vehicle.vehicle_attribute_value import vehicle_attribute_values_schema
from schemas.vehicle.vehicle_year_model import vehicle_year_model_schema, vehicle_year_models_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class VehicleYearModelAction:
    def create(self, data):
        validated_data = vehicle_year_model_schema.load(data)
        entity = VehicleYearModel(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return vehicle_year_model_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleYearModel.query if q == '' else VehicleYearModel.query.filter(
            VehicleYearModel.name.like('%{}%'.format(q)))
        query = query.filter(VehicleYearModel.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleYearModel.name.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleYearModel.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_year_models_schema.dump(items)

        return rv, total

    def get_all_by_vehicle_model_id(self, vehicle_model_id, sort, direction, limit, offset, is_active, q=''):
        current_vehicle_model = VehicleModel.query.get(vehicle_model_id)
        if not current_vehicle_model:
            raise EntityNotFoundException(vehicle_model_id, 'VehicleModel')

        query = VehicleYearModel.query if q == '' else VehicleYearModel.query.filter(
            VehicleYearModel.name.like('%{}%'.format(q)))
        query = query.filter(VehicleYearModel.is_active == is_active) if is_active is not None else query
        query = query.filter(
            VehicleYearModel.vehicle_model_id == vehicle_model_id) if vehicle_model_id is not None else query

        if sort:
            query = query.order_by(
                VehicleYearModel.name.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleYearModel.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_year_models_schema.dump(items)

        return rv, total

    def get(self, id_):
        current_vehicle_year_model = VehicleYearModel.query.get(id_)
        if not current_vehicle_year_model:
            raise EntityNotFoundException(id_, 'VehicleYearModel')

        return vehicle_year_model_schema.dump(current_vehicle_year_model)

    def update(self, id_, data):
        current_vehicle_year_model = VehicleYearModel.query.get(id_)
        if not current_vehicle_year_model:
            raise EntityNotFoundException(id_, 'VehicleYearModel')

        validated_data = vehicle_year_model_schema.load(data)
        validated_data['id'] = None
        current_vehicle_year_model.update(validated_data)
        db.session.commit()

        return vehicle_year_model_schema.dump(current_vehicle_year_model)

    def update_avatar(self, id_, files):

        current_vehicle_year_model = VehicleYearModel.query.get(id_)
        if not current_vehicle_year_model:
            raise EntityNotFoundException(id_, 'VehicleYearModel')

        current_vehicle_year_model._galleries = list(
            filter(lambda g: g.type is not VehicleGalleryItemType.YEAR_MODEL_AVATAR,
                   current_vehicle_year_model._galleries))

        current_vehicle_year_model._galleries.extend(vehicle_gallery_item_action.
                                                     create_gallery_items(VehicleGalleryItemType.YEAR_MODEL_AVATAR,
                                                                          files))

        db.session.commit()
        return vehicle_year_model_schema.dump(current_vehicle_year_model)

    def update_cover(self, id_, files):

        current_vehicle_year_model = VehicleYearModel.query.get(id_)
        if not current_vehicle_year_model:
            raise EntityNotFoundException(id_, 'VehicleYearModel')

        current_vehicle_year_model._galleries = list(
            filter(lambda g: g.type is not VehicleGalleryItemType.COVER, current_vehicle_year_model._galleries))

        current_vehicle_year_model._galleries.extend(vehicle_gallery_item_action.
                                                     create_gallery_items(VehicleGalleryItemType.COVER, files))

        db.session.commit()

        return vehicle_year_model_schema.dump(current_vehicle_year_model)

    def update_introduction_video(self, id_, files):

        current_vehicle_year_model = VehicleYearModel.query.get(id_)
        if not current_vehicle_year_model:
            raise EntityNotFoundException(id_, 'VehicleYearModel')

        current_vehicle_year_model._galleries = list(
            filter(lambda g: g.type is not VehicleGalleryItemType.VIDEO_INTRODUCTION,
                   current_vehicle_year_model._galleries))

        current_vehicle_year_model._galleries.extend(vehicle_gallery_item_action.
                                                     create_gallery_items(VehicleGalleryItemType.VIDEO_INTRODUCTION,
                                                                          files))

        db.session.commit()

        return vehicle_year_model_schema.dump(current_vehicle_year_model)

    def update_exterior(self, id_, files):

        current_vehicle_year_model = VehicleYearModel.query.get(id_)
        if not current_vehicle_year_model:
            raise EntityNotFoundException(id_, 'VehicleYearModel')

        current_vehicle_year_model._galleries = list(
            filter(lambda g: g.type is not VehicleGalleryItemType.EXTERIOR, current_vehicle_year_model._galleries))

        current_vehicle_year_model._galleries.extend(vehicle_gallery_item_action.
                                                     create_gallery_items(VehicleGalleryItemType.EXTERIOR, files))

        db.session.commit()

        return vehicle_year_model_schema.dump(current_vehicle_year_model)

    def update_interior(self, id_, files):

        current_vehicle_year_model = VehicleYearModel.query.get(id_)
        if not current_vehicle_year_model:
            raise EntityNotFoundException(id_, 'VehicleYearModel')

        current_vehicle_year_model._galleries = list(
            filter(lambda g: g.type is not VehicleGalleryItemType.INTERIOR, current_vehicle_year_model._galleries))

        current_vehicle_year_model._galleries.extend(vehicle_gallery_item_action.
                                                     create_gallery_items(VehicleGalleryItemType.INTERIOR, files))

        db.session.commit()

        return vehicle_year_model_schema.dump(current_vehicle_year_model)

    def delete(self, id_):
        vehicle_year_model = VehicleYearModel.query.get(id_)
        if not vehicle_year_model:
            raise EntityNotFoundException(id_, 'VehicleYearModel')

        db.session.delete(vehicle_year_model)
        db.session.commit()

    def update_attribute_values(self, id_, data, is_override=False):
        vehicle_year_model = VehicleYearModel.query.get(id_)
        if not vehicle_year_model:
            raise EntityNotFoundException(id_, 'VehicleModelStyle')

        if is_override:
            vehicle_year_model.attributes = []

        d_vehicle_attribute_values = vehicle_attribute_values_schema.load(data)
        for d_vehicle_attribute_value in d_vehicle_attribute_values:
            vehicle_attribute_value = VehicleAttributeValue(**d_vehicle_attribute_value)
            vehicle_year_model.attributes.append(vehicle_attribute_value)
        db.session.commit()

        return vehicle_year_model_schema.dump(vehicle_year_model)


vehicle_year_model_action = VehicleYearModelAction()
