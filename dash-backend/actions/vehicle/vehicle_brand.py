from flask import request

from actions.vehicle.vehicle_gallery_item import vehicle_gallery_item_action
from models import db
from models.vehicle.vehicle_brand import VehicleBrand
from models.vehicle.vehicle_gallery_item import VehicleGalleryItemType
from schemas.vehicle.vehicle_brand import vehicle_brand_schema, vehicle_brands_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class VehicleBrandAction:
    def create(self, data):
        validated_data = vehicle_brand_schema.load(data)
        entity = VehicleBrand(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return vehicle_brand_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleBrand.query if q == '' else VehicleBrand.query.filter(VehicleBrand.name.like('%{}%'.format(q)))
        query = query.filter(VehicleBrand.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleBrand.name.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleBrand.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_brands_schema.dump(items)

        return rv, total

    def get(self, id_):
        current_vehicle_brand = VehicleBrand.query.get(id_)
        if not current_vehicle_brand:
            raise EntityNotFoundException(id_, 'VehicleBrand')

        return vehicle_brand_schema.dump(current_vehicle_brand)

    def update(self, id_, data):
        current_vehicle_brand = VehicleBrand.query.get(id_)
        if not current_vehicle_brand:
            raise EntityNotFoundException(id_, 'VehicleBrand')

        validated_data = vehicle_brand_schema.load(data)
        validated_data['id'] = None
        current_vehicle_brand.update(validated_data)
        db.session.commit()

        return vehicle_brand_schema.dump(current_vehicle_brand)

    def update_logo(self, id_, files):
        current_vehicle_brand = VehicleBrand.query.get(id_)
        if not current_vehicle_brand:
            raise EntityNotFoundException(id_, 'VehicleBrand')

        current_vehicle_brand._galleries = list(
            filter(lambda g: g.type is not VehicleGalleryItemType.BRAND_LOGO, current_vehicle_brand._galleries))

        current_vehicle_brand._galleries.extend(vehicle_gallery_item_action. \
                                                create_gallery_items(VehicleGalleryItemType.BRAND_LOGO, files))

        db.session.commit()

        return vehicle_brand_schema.dump(current_vehicle_brand)

    def delete(self, id_):
        vehicle_brand = VehicleBrand.query.get(id_)
        if not vehicle_brand:
            raise EntityNotFoundException(id_, 'VehicleBrand')

        db.session.delete(vehicle_brand)
        db.session.commit()


vehicle_brand_action = VehicleBrandAction()
