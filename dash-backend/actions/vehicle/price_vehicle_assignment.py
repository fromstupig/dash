from models import db
from models.vehicle.price_vehicle_assignment import PriceVehicleAssignment
from schemas.vehicle.price_vehicle_assignment import price_vehicle_assignment_schema, price_vehicle_assignments_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class PriceVehicleAssignmentAction:
    def create(self, data):
        validated_data = price_vehicle_assignment_schema.load(data)
        entity = PriceVehicleAssignment(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return price_vehicle_assignment_schema.dump(entity)

    def get(self, id_):
        current_price_vehicle_assignments = PriceVehicleAssignment.query.get(id_)
        if not current_price_vehicle_assignments:
            raise EntityNotFoundException(id_, 'PriceVehicleAssignment')
        else:
            return price_vehicle_assignments_schema.dump(current_price_vehicle_assignments)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = PriceVehicleAssignment.query
        query = query.filter(PriceVehicleAssignment.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                PriceVehicleAssignment.start_date.asc()) if direction == SortDirection.ASC else query.order_by(
                PriceVehicleAssignment.start_date.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = price_vehicle_assignments_schema.dump(items)

        return rv, total

    def update(self, id_, data):
        current_price_vehicle_assignment = PriceVehicleAssignment.query.get(id_)
        if not current_price_vehicle_assignment:
            raise EntityNotFoundException(id_, 'PriceVehicleAssignment')

        validated_data = price_vehicle_assignment_schema.load(data)
        validated_data['id'] = None
        entity = PriceVehicleAssignment(**validated_data)
        db.session.add(entity)

        db.session.commit()
        return price_vehicle_assignment_schema.dump(entity)

    def delete(self, id_):
        price_vehicle_assignment = PriceVehicleAssignment.query.get(id_)
        if not price_vehicle_assignment:
            raise EntityNotFoundException(id_, 'PriceVehicleAssignment')

        db.session.delete(price_vehicle_assignment)
        db.session.commit()


price_vehicle_assignment_action = PriceVehicleAssignmentAction()
