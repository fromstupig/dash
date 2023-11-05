from models import db
from models.vehicle.vehicle_attribute_value import VehicleAttributeValue
from schemas.vehicle.vehicle_attribute_value import vehicle_attribute_value_schema, vehicle_attribute_values_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class VehicleAttributeValueAction:
    def create(self, data):
        validated_data = vehicle_attribute_value_schema.load(data)
        entity = VehicleAttributeValue(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return vehicle_attribute_value_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleAttributeValue.query if q == '' else VehicleAttributeValue.query.filter(
            VehicleAttributeValue.name.like('%{}%'.format(q)))
        query = query.filter(VehicleAttributeValue.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleAttributeValue.name.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleAttributeValue.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_attribute_values_schema.dump(items)

        return rv, total

    def update(self, id_, data):
        current_vehicle_attribute_value = VehicleAttributeValue.query.get(id_)
        if not current_vehicle_attribute_value:
            raise EntityNotFoundException(id_, 'VehicleAttributeValue')

        validated_data = vehicle_attribute_value_schema.load(data)
        validated_data['id'] = None
        entity = VehicleAttributeValue(**validated_data)
        db.session.add(entity)

        db.session.commit()
        return vehicle_attribute_value_schema.dump(entity)

    def delete(self, id_):
        vehicle_attribute_value = VehicleAttributeValue.query.get(id_)
        if not vehicle_attribute_value:
            raise EntityNotFoundException(id_, 'VehicleAttributeValue')

        db.session.delete(vehicle_attribute_value)
        db.session.commit()


vehicle_attribute_value_action = VehicleAttributeValueAction()
