from flask import request

from actions.vehicle.vehicle_gallery_item import vehicle_gallery_item_action
from models import db
from models.vehicle import VehicleBrand
from models.vehicle.vehicle_gallery_item import VehicleGalleryItemType
from models.vehicle.vehicle_model import VehicleModel
from schemas.vehicle.vehicle_model import vehicle_model_schema, vehicle_models_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class VehicleModelAction:
    def create(self, data):
        validated_data = vehicle_model_schema.load(data)
        entity = VehicleModel(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return vehicle_model_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleModel.query if q == '' else VehicleModel.query.filter(VehicleModel.name.like('%{}%'.format(q)))
        query = query.filter(VehicleModel.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleModel.name.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleModel.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_models_schema.dump(items)

        return rv, total

    def get_all_by_vehicle_brand_id(self, vehicle_brand_id, sort, direction, limit, offset, is_active, q=''):
        current_vehicle_brand = VehicleBrand.query.get(vehicle_brand_id)
        if not current_vehicle_brand:
            raise EntityNotFoundException(vehicle_brand_id, 'VehicleBrand')

        query = VehicleModel.query if q == '' else VehicleModel.query.filter(VehicleModel.name.like('%{}%'.format(q)))
        query = query.filter(VehicleModel.is_active == is_active) if is_active is not None else query
        query = query.filter(
            VehicleModel.vehicle_brand_id == vehicle_brand_id) if vehicle_brand_id is not None else query

        if sort:
            query = query.order_by(
                VehicleModel.name.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleModel.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_models_schema.dump(items)

        return rv, total

    def get(self, id_):
        current_vehicle_model = VehicleModel.query.get(id_)
        if not current_vehicle_model:
            raise EntityNotFoundException(id_, 'VehicleModel')

        return vehicle_model_schema.dump(current_vehicle_model)

    def update(self, id_, data):
        current_vehicle_model = VehicleModel.query.get(id_)
        if not current_vehicle_model:
            raise EntityNotFoundException(id_, 'VehicleModel')

        validated_data = vehicle_model_schema.load(data)
        validated_data['id'] = None
        current_vehicle_model.update(validated_data)
        db.session.commit()

        return vehicle_model_schema.dump(current_vehicle_model)

    def update_avatar(self, id_, files):
        current_vehicle_model = VehicleModel.query.get(id_)
        if not current_vehicle_model:
            raise EntityNotFoundException(id_, 'VehicleModel')

        current_vehicle_model._galleries = list(
            filter(lambda g: g.type is not VehicleGalleryItemType.MODEL_AVATAR, current_vehicle_model._galleries))

        current_vehicle_model._galleries.extend(vehicle_gallery_item_action. \
                                                create_gallery_items(VehicleGalleryItemType.MODEL_AVATAR, files))

        db.session.commit()

        return vehicle_model_schema.dump(current_vehicle_model)

    def delete(self, id_):
        vehicle_model = VehicleModel.query.get(id_)
        if not vehicle_model:
            raise EntityNotFoundException(id_, 'VehicleModel')

        db.session.delete(vehicle_model)
        db.session.commit()


vehicle_model_action = VehicleModelAction()
