from marshmallow import fields

from models.dealer.dealer_scheduler import DealerScheduler
from schemas.vehicle import VehicleSchema
from schemas.authorization.user import UserSchema
from schemas.base import IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema, MultiDealerSchema


class DealerSchedulerSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema, MultiDealerSchema):
    __model__ = DealerScheduler

    schedule_title = fields.String()
    schedule_time = fields.DateTime()
    schedule_note = fields.String()

    vehicle_id = fields.Integer()
    vehicle = fields.Nested(VehicleSchema, many=False)

    user_id = fields.Integer()
    user = fields.Nested(UserSchema, many=False)


dealer_scheduler_schema = DealerSchedulerSchema()
dealer_schedulers_schema = DealerSchedulerSchema(many=True)
