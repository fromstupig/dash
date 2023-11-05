from marshmallow import fields

from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema
from schemas.vehicle.vehicle_attribute_value import VehicleAttributeValueSchema


class VehicleYearModelAttributeSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    vehicle_year_model_id = fields.Integer()
    vehicle_attribute_value_id = fields.Integer()

    vehicle_attribute_value = fields.Nested(VehicleAttributeValueSchema)


vehicle_year_model_attribute_schema = VehicleYearModelAttributeSchema()
vehicle_year_model_attributes_schema = VehicleYearModelAttributeSchema(many=True)
