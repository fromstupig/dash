from marshmallow import fields, EXCLUDE

from models.vehicle import VehicleHistory
from schemas.authorization.user import UserSchema
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema
from schemas.vehicle.vehicle_status import VehicleStatusSchema


class VehicleHistorySchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    __model__ = VehicleHistory

    class Meta:
        unknown = EXCLUDE

    vehicle_id = fields.Integer()
    purchased_date = fields.DateTime(required=True)
    owner_id = fields.Integer()
    owner = fields.Nested(UserSchema, many=False)

    statuses = fields.Nested(VehicleStatusSchema, many=True)


vehicle_history_schema = VehicleHistorySchema()
vehicle_histories_schema = VehicleHistorySchema(many=True)
