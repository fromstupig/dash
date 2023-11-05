from models import db
from models.vehicle.vehicle_attribute import VehicleAttribute
from schemas.vehicle.vehicle_attribute import vehicle_attribute_schema, vehicle_attributes_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class VehicleAttributeAction:
    def create(self, data):
        validated_data = vehicle_attribute_schema.load(data)
        entity = VehicleAttribute(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return vehicle_attribute_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleAttribute.query if q == '' else VehicleAttribute.query.filter(
            VehicleAttribute.name.like('%{}%'.format(q)))
        query = query.filter(VehicleAttribute.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleAttribute.name.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleAttribute.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_attributes_schema.dump(items)

        return rv, total

    def get(self, id_):
        current_vehicle_attribute = VehicleAttribute.query.get(id_)
        if not current_vehicle_attribute:
            raise EntityNotFoundException(id_, 'VehicleAttribute')

        return vehicle_attribute_schema.dump(current_vehicle_attribute)

    def update(self, id_, data):
        current_vehicle_attribute = VehicleAttribute.query.get(id_)
        if not current_vehicle_attribute:
            raise EntityNotFoundException(id_, 'VehicleAttribute')

        validated_data = vehicle_attribute_schema.load(data)
        validated_data['id'] = None
        current_vehicle_attribute.update(validated_data)

        db.session.commit()
        return vehicle_attribute_schema.dump(current_vehicle_attribute)

    def delete(self, id_):
        vehicle_attribute = VehicleAttribute.query.get(id_)
        if not vehicle_attribute:
            raise EntityNotFoundException(id_, 'VehicleAttribute')

        db.session.delete(vehicle_attribute)
        db.session.commit()


vehicle_attribute_action = VehicleAttributeAction()
