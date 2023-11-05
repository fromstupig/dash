from marshmallow import fields, EXCLUDE

from models.vehicle import PriceOptionAssignment
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema, PriceAssignmentSchema


class PriceOptionAssignmentSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PriceAssignmentSchema):
    __model__ = PriceOptionAssignment

    class Meta:
        unknown = EXCLUDE

    vehicle_option_item_id = fields.Integer()


price_option_assignment_schema = PriceOptionAssignmentSchema()
price_option_assignments_schema = PriceOptionAssignmentSchema(many=True)
