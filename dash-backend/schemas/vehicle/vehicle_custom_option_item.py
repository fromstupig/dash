from marshmallow import fields, EXCLUDE

from models.vehicle.vehicle_custom_option_item import VehicleCustomOptionItem
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema


class VehicleCustomOptionSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    __model__ = VehicleCustomOptionItem

    class Meta:
        unknown = EXCLUDE

    vehicle_id = fields.Integer()
    vehicle_option_item_id = fields.Integer()


vehicle_custom_option_schema = VehicleCustomOptionSchema()
vehicle_custom_options_schema = VehicleCustomOptionSchema(many=True)
