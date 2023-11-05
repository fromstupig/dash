from models import db
from models.vehicle.vehicle_history import VehicleHistory
from schemas.vehicle.vehicle_history import vehicle_history_schema, vehicle_histories_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class VehicleHistoryAction:
    def create(self, data):
        validated_data = vehicle_history_schema.load(data)
        entity = VehicleHistory(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return vehicle_history_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleHistory.query
        query = query.filter(VehicleHistory.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleHistory.vehicle_id.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleHistory.vehicle_id.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_histories_schema.dump(items)

        return rv, total

    def update(self, id_, data):
        current_vehicle_history = VehicleHistory.query.get(id_)
        if not current_vehicle_history:
            raise EntityNotFoundException(id_, 'VehicleHistory')

        validated_data = vehicle_history_schema.load(data)
        validated_data['id'] = None
        entity = VehicleHistory(**validated_data)
        db.session.add(entity)

        db.session.commit()
        return vehicle_history_schema.dump(entity)

    def delete(self, id_):
        vehicle_history = VehicleHistory.query.get(id_)
        if not vehicle_history:
            raise EntityNotFoundException(id_, 'VehicleHistory')

        db.session.delete(vehicle_history)
        db.session.commit()


vehicle_history_action = VehicleHistoryAction()
