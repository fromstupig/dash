from marshmallow import fields

from models.dealer.dealer import Dealer
from schemas.base import IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema
from schemas.core_provider.address import AddressSchema


class DealerSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema):
    __model__ = Dealer

    name = fields.String(required=True)
    website = fields.String()
    phone = fields.String()
    address = fields.Nested(AddressSchema, many=True)
    lat = fields.Float()
    long = fields.Float()


dealer_schema = DealerSchema()
dealers_schema = DealerSchema(many=True)
