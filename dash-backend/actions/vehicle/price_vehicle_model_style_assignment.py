from models import db
from models.vehicle.price_vehicle_model_style_assignment import PriceVehicleModelStyleAssignment
from schemas.vehicle.price_vehicle_model_style_assignment import price_vehicle_model_style_assignment_schema, \
    price_vehicle_model_style_assignments_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class PriceVehicleModelStyleAssignmentAction:
    def create(self, data):
        validated_data = price_vehicle_model_style_assignment_schema.load(data)
        entity = PriceVehicleModelStyleAssignment(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return price_vehicle_model_style_assignment_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = PriceVehicleModelStyleAssignment.query
        query = query.filter(
            PriceVehicleModelStyleAssignment.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                PriceVehicleModelStyleAssignment.start_date.asc()) if direction == SortDirection.ASC else query.order_by(
                PriceVehicleModelStyleAssignment.start_date.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = price_vehicle_model_style_assignments_schema.dump(items)

        return rv, total

    def update(self, id_, data):
        current_price_vehicle_model_style_assignment = PriceVehicleModelStyleAssignment.query.get(id_)
        if not current_price_vehicle_model_style_assignment:
            raise EntityNotFoundException(id_, 'PriceVehicleModelStyleAssignment')

        validated_data = price_vehicle_model_style_assignment_schema.load(data)
        validated_data['id'] = None
        entity = PriceVehicleModelStyleAssignment(**validated_data)
        db.session.add(entity)

        db.session.commit()
        return price_vehicle_model_style_assignment_schema.dump(entity)

    def delete(self, id_):
        price_vehicle_model_style_assignment = PriceVehicleModelStyleAssignment.query.get(id_)
        if not price_vehicle_model_style_assignment:
            raise EntityNotFoundException(id_, 'PriceVehicleModelStyleAssignment')

        db.session.delete(price_vehicle_model_style_assignment)
        db.session.commit()


price_vehicle_model_style_assignment_action = PriceVehicleModelStyleAssignmentAction()
