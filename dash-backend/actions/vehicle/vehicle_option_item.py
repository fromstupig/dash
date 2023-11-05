from actions.vehicle.vehicle_gallery_item import vehicle_gallery_item_action
from models import db
from models.vehicle.vehicle_gallery_item import VehicleGalleryItemType
from models.vehicle.vehicle_option_item import VehicleOptionItem
from schemas.vehicle.vehicle_option_item import vehicle_option_item_schema, vehicle_option_items_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class VehicleOptionItemAction:
    def create(self, data):
        validated_data = vehicle_option_item_schema.load(data)
        entity = VehicleOptionItem(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return vehicle_option_item_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleOptionItem.query if q == '' else VehicleOptionItem.query.filter(
            VehicleOptionItem.name.like('%{}%'.format(q)))
        query = query.filter(VehicleOptionItem.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleOptionItem.name.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleOptionItem.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_option_items_schema.dump(items)

        return rv, total

    def get(self, id_):
        current_vehicle_option_item = VehicleOptionItem.query.get(id_)
        if not current_vehicle_option_item:
            raise EntityNotFoundException(id_, 'VehicleOptionItem')

        return vehicle_option_item_schema.dump(current_vehicle_option_item)

    def update(self, id_, data):
        current_vehicle_option_item = VehicleOptionItem.query.get(id_)
        if not current_vehicle_option_item:
            raise EntityNotFoundException(id_, 'VehicleOptionItem')

        validated_data = vehicle_option_item_schema.load(data)
        validated_data['id'] = None
        current_vehicle_option_item.update(validated_data)
        db.session.commit()

        return vehicle_option_item_schema.dump(current_vehicle_option_item)

    def update_avatar(self, id_, files):

        current_vehicle_option_item = VehicleOptionItem.query.get(id_)
        if not current_vehicle_option_item:
            raise EntityNotFoundException(id_, 'VehicleOptionItem')

        current_vehicle_option_item._galleries = list(
            filter(lambda g: g.type is not VehicleGalleryItemType.OPTION_ITEM_AVATAR,
                   current_vehicle_option_item._galleries))

        current_vehicle_option_item._galleries.extend(vehicle_gallery_item_action. \
                                                      create_gallery_items(VehicleGalleryItemType.OPTION_ITEM_AVATAR,
                                                                           files))

        db.session.commit()

        return vehicle_option_item_schema.dump(current_vehicle_option_item)

    def delete(self, id_):
        vehicle_option_item = VehicleOptionItem.query.get(id_)
        if not vehicle_option_item:
            raise EntityNotFoundException(id_, 'VehicleOptionItem')

        db.session.delete(vehicle_option_item)
        db.session.commit()


vehicle_option_item_action = VehicleOptionItemAction()
