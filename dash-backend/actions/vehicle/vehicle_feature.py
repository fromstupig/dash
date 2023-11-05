from models.vehicle import VehicleEngine, VehicleTransmission, VehicleBody, VehicleDriveTrain
from models.vehicle.vehicle import Vehicle
from schemas.vehicle.vehicle_feature import vehicle_engines_schema, vehicle_transmissions_schema, vehicle_bodies_schema, \
    vehicle_drive_trains_schema
from utilities.enum import SortDirection


class VehicleFeatureAction:
    def get_all_engine(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleEngine.query if q == '' else VehicleEngine.query.filter(
            VehicleEngine.label.like('%{}%'.format(q)))
        query = query.filter(VehicleEngine.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleEngine.label.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleEngine.label.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_engines_schema.dump(items)

        return rv, total

    def get_all_transmission(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleTransmission.query if q == '' else VehicleTransmission.query.filter(
            VehicleTransmission.label.like('%{}%'.format(q)))
        query = query.filter(VehicleTransmission.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleTransmission.label.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleTransmission.label.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_transmissions_schema.dump(items)

        return rv, total

    def get_all_drive_train(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleDriveTrain.query if q == '' else VehicleDriveTrain.query.filter(
            VehicleDriveTrain.name.like('%{}%'.format(q)))
        query = query.filter(VehicleDriveTrain.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleDriveTrain.name.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleDriveTrain.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_drive_trains_schema.dump(items)

        return rv, total

    def get_all_body(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleBody.query if q == '' else VehicleBody.query.filter(VehicleBody.name.like('%{}%'.format(q)))
        query = query.filter(VehicleBody.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleBody.name.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleBody.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_bodies_schema.dump(items)

        return rv, total


vehicle_feature_action = VehicleFeatureAction()
