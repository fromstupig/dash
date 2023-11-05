from models import db
from models.vehicle.vehicle_status import VehicleStatus
from schemas.vehicle.vehicle_status import vehicle_status_schema, vehicle_statuses_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class VehicleStatusAction:
    def create(self, data):
        validated_data = vehicle_status_schema.load(data)
        entity = VehicleStatus(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return vehicle_status_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleStatus.query
        query = query.filter(VehicleStatus.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleStatus.checked_date.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleStatus.checked_date.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_statuses_schema.dump(items)

        return rv, total

    def update(self, id_, data):
        current_vehicle_status = VehicleStatus.query.get(id_)
        if not current_vehicle_status:
            raise EntityNotFoundException(id_, 'VehicleStatus')

        validated_data = vehicle_status_schema.load(data)
        validated_data['id'] = None
        entity = VehicleStatus(**validated_data)
        db.session.add(entity)

        db.session.commit()
        return vehicle_status_schema.dump(entity)

    def delete(self, id_):
        vehicle_status = VehicleStatus.query.get(id_)
        if not vehicle_status:
            raise EntityNotFoundException(id_, 'VehicleStatus')

        db.session.delete(vehicle_status)
        db.session.commit()


vehicle_status_action = VehicleStatusAction()
