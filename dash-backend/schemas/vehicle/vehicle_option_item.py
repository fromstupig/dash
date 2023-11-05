from marshmallow import fields, EXCLUDE
from marshmallow_enum import EnumField

from models.vehicle.vehicle_option_item import VehicleOptionItem
from models.vehicle.vehicle_option_item import VehicleOptionGroupType
from schemas.vehicle.price_option_assignment import PriceOptionAssignmentSchema

from schemas.vehicle.vehicle_gallery_item import VehicleGalleryItemSchema
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema


class VehicleOptionItemSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    __model__ = VehicleOptionItem

    class Meta:
        unknown = EXCLUDE

    description = fields.String(required=True)
    detail = fields.Dict()
    is_popular = fields.Boolean()
    type = EnumField(VehicleOptionGroupType, required=True)
    galleries = fields.Nested(VehicleGalleryItemSchema, many=True)
    current_price_assigment = fields.Nested(PriceOptionAssignmentSchema, many=True)


vehicle_option_item_schema = VehicleOptionItemSchema()
vehicle_option_items_schema = VehicleOptionItemSchema(many=True)
