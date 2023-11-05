from marshmallow import fields, EXCLUDE

from models.vehicle import VehicleBrand
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema
from schemas.vehicle.vehicle_gallery_item import VehicleGalleryItemSchema


class VehicleBrandSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    __model__ = VehicleBrand

    class Meta:
        unknown = EXCLUDE

    name = fields.String(required=True)
    description = fields.String(required=True)

    galleries = fields.Nested(VehicleGalleryItemSchema, many=True)


vehicle_brand_schema = VehicleBrandSchema()
vehicle_brands_schema = VehicleBrandSchema(many=True)
