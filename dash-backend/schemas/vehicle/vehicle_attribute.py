from marshmallow import fields, EXCLUDE

from models.vehicle import VehicleAttribute
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema


class VehicleAttributeSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    __model__ = VehicleAttribute

    class Meta:
        unknown = EXCLUDE

    name = fields.String(required=True)
    description = fields.String(required=True)

    parent_id = fields.Integer()
    parent = fields.Nested('VehicleAttributeSchema', many=False, dump_only=True)


vehicle_attribute_schema = VehicleAttributeSchema()
vehicle_attributes_schema = VehicleAttributeSchema(many=True)
