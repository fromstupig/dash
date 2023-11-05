from flask import request

from actions.vehicle.vehicle_gallery_item import vehicle_gallery_item_action
from models import db
from models.vehicle.vehicle import Vehicle
from models.vehicle.vehicle_gallery_item import VehicleGalleryItemType
from schemas.vehicle.vehicle import vehicle_schema, vehicles_schema
from services.search import SearchService
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class VehicleAction:
    def create(self, data):
        validated_data = vehicle_schema.load(data)
        entity = Vehicle(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return vehicle_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = Vehicle.query if q == '' else Vehicle.query.filter(Vehicle.name.like('%{}%'.format(q)))
        query = query.filter(Vehicle.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                Vehicle.name.asc()) if direction == SortDirection.ASC else query.order_by(
                Vehicle.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicles_schema.dump(items)

        return rv, total

    def get(self, id_):
        current_vehicle = Vehicle.query.get(id_)
        if not current_vehicle:
            raise EntityNotFoundException(id_, 'Vehicle')

        return vehicle_schema.dump(current_vehicle)

    def update(self, id_, data):
        current_vehicle = Vehicle.query.get(id_)
        if not current_vehicle:
            raise EntityNotFoundException(id_, 'Vehicle')

        validated_data = vehicle_schema.load(data)
        validated_data['id'] = None
        current_vehicle.update(validated_data)
        db.session.commit()

        return vehicle_schema.dump(current_vehicle)

    def update_avatar(self, id_, files):

        current_vehicle = Vehicle.query.get(id_)
        if not current_vehicle:
            raise EntityNotFoundException(id_, 'Vehicle')

        current_vehicle._galleries = list(
            filter(lambda g: g.type is not VehicleGalleryItemType.VEHICLE_AVATAR, current_vehicle._galleries))

        current_vehicle._galleries.extend(vehicle_gallery_item_action. \
                                          create_gallery_items(VehicleGalleryItemType.VEHICLE_AVATAR, files))

        db.session.commit()

        return vehicle_schema.dump(current_vehicle)

    def delete(self, id_):
        vehicle = Vehicle.query.get(id_)
        if not vehicle:
            raise EntityNotFoundException(id_, 'Vehicle')

        db.session.delete(vehicle)
        db.session.commit()

    def search(self, vehicle_search_params):
        search_service = SearchService()
        result, total = search_service.search_vehicle(vehicle_search_params)

        return result, total


vehicle_action = VehicleAction()
