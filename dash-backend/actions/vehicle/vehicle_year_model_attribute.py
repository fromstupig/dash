from models import db
from models.vehicle.vehicle_year_model_attribute import VehicleYearModelAttribute
from schemas.vehicle.vehicle_year_model_attribute import vehicle_year_model_attribute_schema, \
    vehicle_year_model_attributes_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class VehicleYearModelAttributeAction:
    def create(self, data):
        validated_data = vehicle_year_model_attribute_schema.load(data)
        entity = VehicleYearModelAttribute(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return vehicle_year_model_attribute_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleYearModelAttribute.query
        query = query.filter(VehicleYearModelAttribute.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleYearModelAttribute.vehicle_model_style_id.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleYearModelAttribute.vehicle_model_style_id.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_year_model_attributes_schema.dump(items)

        return rv, total

    def update(self, id_, data):
        current_vehicle_year_model_attribute = VehicleYearModelAttribute.query.get(id_)
        if not current_vehicle_year_model_attribute:
            raise EntityNotFoundException(id_, 'VehicleYearModelAttribute')

        validated_data = vehicle_year_model_attribute_schema.load(data)
        validated_data['id'] = None
        entity = VehicleYearModelAttribute(**validated_data)
        db.session.add(entity)

        db.session.commit()
        return vehicle_year_model_attribute_schema.dump(entity)

    def delete(self, id_):
        vehicle_year_model_attribute = VehicleYearModelAttribute.query.get(id_)
        if not vehicle_year_model_attribute:
            raise EntityNotFoundException(id_, 'VehicleYearModelAttribute')

        db.session.delete(vehicle_year_model_attribute)
        db.session.commit()


vehicle_year_model_attribute_action = VehicleYearModelAttributeAction()
