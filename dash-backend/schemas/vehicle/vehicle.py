from marshmallow import fields, EXCLUDE

from models.vehicle import Vehicle
from schemas.vehicle.vehicle_option_item import VehicleOptionItemSchema
from schemas.vehicle.vehicle_model_style import VehicleModelStyleSchema
from schemas.vehicle.vehicle_model import VehicleModelSchema
from schemas.vehicle.vehicle_brand import VehicleBrandSchema
from schemas.vehicle.vehicle_gallery_item import VehicleGalleryItemSchema
from schemas.authorization.user import UserSchema
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema
from schemas.vehicle.price_vehicle_assignment import PriceVehicleAssignmentSchema
from schemas.vehicle.vehicle_custom_attribute import VehicleCustomAttributeSchema
from schemas.vehicle.vehicle_custom_option_item import VehicleCustomOptionSchema
from schemas.vehicle.vehicle_history import VehicleHistorySchema


class VehicleSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    __model__ = Vehicle

    class Meta:
        unknown = EXCLUDE

    name = fields.String(required=True)
    description = fields.String(required=True)

    vehicle_brand_id = fields.Integer()
    vehicle_brand = fields.Nested(VehicleBrandSchema, only=['name', 'description'], dump_only=True)

    vehicle_model_id = fields.Integer()
    vehicle_model = fields.Nested(VehicleModelSchema, only=['name', 'description'], dump_only=True)

    vehicle_model_style_id = fields.Integer()
    vehicle_model_style = fields.Nested(VehicleModelStyleSchema, dump_only=True)

    current_owner_id = fields.Integer()
    current_owner = fields.Nested(UserSchema, many=False)

    current_price_assigment = fields.Nested(PriceVehicleAssignmentSchema, many=False)
    custom_options = fields.Nested(VehicleOptionItemSchema, many=True)
    galleries = fields.Nested(VehicleGalleryItemSchema, many=True)


vehicle_schema = VehicleSchema()
els_vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)
