from marshmallow import fields, EXCLUDE
from marshmallow_enum import EnumField

from models.vehicle.vehicle_gallery_item import VehicleGalleryItemType, VehicleGalleryItem
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema
from utilities.constant import get_s3_location


class VehicleGalleryItemSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    __model__ = VehicleGalleryItem

    class Meta:
        unknown = EXCLUDE

    type = EnumField(VehicleGalleryItemType, required=True)
    order = fields.Integer()
    asset_path = fields.String(required=True)


vehicle_gallery_item_schema = VehicleGalleryItemSchema()
vehicle_gallery_items_schema = VehicleGalleryItemSchema(many=True)
