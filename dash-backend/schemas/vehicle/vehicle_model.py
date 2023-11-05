from marshmallow import fields, EXCLUDE

from models.vehicle import VehicleModel
from schemas.vehicle.vehicle_gallery_item import VehicleGalleryItemSchema
from schemas.vehicle.vehicle_brand import VehicleBrandSchema
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema


class VehicleModelSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    __model__ = VehicleModel

    class Meta:
        unknown = EXCLUDE

    name = fields.String(required=True)
    description = fields.String(required=True)

    vehicle_brand_id = fields.Integer()
    vehicle_brand = fields.Nested(VehicleBrandSchema, only=['name', 'description'], dump_only=True)

    galleries = fields.Nested(VehicleGalleryItemSchema, many=True)

vehicle_model_schema = VehicleModelSchema()
vehicle_models_schema = VehicleModelSchema(many=True)
