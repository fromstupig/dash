from marshmallow import fields, EXCLUDE

from models.vehicle import VehicleCustomAttribute
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema


class VehicleCustomAttributeSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    __model__ = VehicleCustomAttribute

    class Meta:
        unknown = EXCLUDE

    vehicle_id = fields.Integer()
    vehicle_attribute_value_id = fields.Integer()


vehicle_custom_attribute_schema = VehicleCustomAttributeSchema()
vehicle_custom_attributes_schema = VehicleCustomAttributeSchema(many=True)
