from marshmallow import fields

from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema
from schemas.vehicle.vehicle_attribute_value import VehicleAttributeValueSchema


class VehicleModelStyleAttributeSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    vehicle_model_style_id = fields.Integer()

    vehicle_attribute_value_id = fields.Integer()
    vehicle_attribute_value = fields.Nested(VehicleAttributeValueSchema)


vehicle_model_style_attribute_schema = VehicleModelStyleAttributeSchema()
vehicle_model_style_attributes_schema = VehicleModelStyleAttributeSchema(many=True)
