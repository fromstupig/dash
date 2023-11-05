from models import db
from models.vehicle.vehicle_model_style_attribute import VehicleModelStyleAttribute
from schemas.vehicle.vehicle_model_style_attribute import vehicle_model_style_attribute_schema, \
    vehicle_model_style_attributes_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class VehicleModelStyleAttributeAction:
    def create(self, data):
        validated_data = vehicle_model_style_attribute_schema.load(data)
        entity = VehicleModelStyleAttribute(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return vehicle_model_style_attribute_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleModelStyleAttribute.query
        query = query.filter(VehicleModelStyleAttribute.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleModelStyleAttribute.vehicle_model_style_id.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleModelStyleAttribute.vehicle_model_style_id.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_model_style_attributes_schema.dump(items)

        return rv, total

    def update(self, id_, data):
        current_vehicle_model_style_attribute = VehicleModelStyleAttribute.query.get(id_)
        if not current_vehicle_model_style_attribute:
            raise EntityNotFoundException(id_, 'VehicleModelStyleAttribute')

        validated_data = vehicle_model_style_attribute_schema.load(data)
        validated_data['id'] = None
        entity = VehicleModelStyleAttribute(**validated_data)
        db.session.add(entity)

        db.session.commit()
        return vehicle_model_style_attribute_schema.dump(entity)

    def delete(self, id_):
        vehicle_model_style_attribute = VehicleModelStyleAttribute.query.get(id_)
        if not vehicle_model_style_attribute:
            raise EntityNotFoundException(id_, 'VehicleModelStyleAttribute')

        db.session.delete(vehicle_model_style_attribute)
        db.session.commit()


vehicle_model_style_attribute_action = VehicleModelStyleAttributeAction()
