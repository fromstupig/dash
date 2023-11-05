from marshmallow import fields, EXCLUDE

from models.vehicle import VehicleStatus
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema


class VehicleStatusSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    __model__ = VehicleStatus

    class Meta:
        unknown = EXCLUDE

    checked_date = fields.DateTime(required=True)
    mileage = fields.Float()
    note = fields.String()

    vehicle_history_id = fields.Integer()


vehicle_status_schema = VehicleStatusSchema()
vehicle_statuses_schema = VehicleStatusSchema(many=True)
