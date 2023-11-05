from marshmallow import fields, EXCLUDE

from models.vehicle import VehicleAttributeValue
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema
from schemas.vehicle.vehicle_attribute import VehicleAttributeSchema


class VehicleAttributeValueSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    __model__ = VehicleAttributeValue

    class Meta:
        unknown = EXCLUDE

    value = fields.String(required=True)
    value_in_number = fields.Float()

    vehicle_attribute_id = fields.Integer()
    vehicle_attribute = fields.Nested(VehicleAttributeSchema, many=False, dump_only=True)


vehicle_attribute_value_schema = VehicleAttributeValueSchema()
vehicle_attribute_values_schema = VehicleAttributeValueSchema(many=True)


class VehicleYearModelAttributeSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    vehicle_year_model_id = fields.Integer()
    vehicle_attribute_value_id = fields.Integer()


vehicle_year_model_attribute_schema = VehicleYearModelAttributeSchema()
vehicle_year_model_attributes_schema = VehicleYearModelAttributeSchema(many=True)


class VehicleModelStyleAttributeSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    vehicle_model_style_id = fields.Integer()
    vehicle_attribute_value_id = fields.Integer()


vehicle_model_style_attribute_schema = VehicleModelStyleAttributeSchema()
vehicle_model_style_attributes_schema = VehicleModelStyleAttributeSchema(many=True)
