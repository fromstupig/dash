from marshmallow import fields
from marshmallow_enum import EnumField

from models.dealer.dealer_request import DealerRequest, RequestStatus
from schemas.core_provider.address import AddressSchema
from schemas.vehicle import VehicleSchema
from schemas.authorization.user import UserSchema
from schemas.base import IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema, MultiDealerSchema


class DealerRequestSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema, MultiDealerSchema):
    __model__ = DealerRequest

    requester_email = fields.String()
    requester_phone_number = fields.String()

    vehicle_id = fields.Integer(required=True)
    vehicle = fields.Nested(VehicleSchema, many=False)

    user_id = fields.Integer()
    user = fields.Nested(UserSchema, many=False)

    pricing_detail = fields.Dict()
    credit_information = fields.Dict()
    dealer_option = fields.Dict()

    address = fields.Nested(AddressSchema, many=True)

    status = EnumField(RequestStatus, default=RequestStatus.PENDING)


dealer_request_schema = DealerRequestSchema()
dealer_requests_schema = DealerRequestSchema(many=True)
