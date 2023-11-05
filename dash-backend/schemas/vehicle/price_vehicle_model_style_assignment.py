from marshmallow import fields, EXCLUDE

from models.vehicle import PriceVehicleModelStyleAssignment
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema, PriceAssignmentSchema


class PriceVehicleModelStyleAssignmentSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema,
                                             PriceAssignmentSchema):
    __model__ = PriceVehicleModelStyleAssignment

    class Meta:
        unknown = EXCLUDE

    vehicle_model_style_id = fields.Integer()


price_vehicle_model_style_assignment_schema = PriceVehicleModelStyleAssignmentSchema()
price_vehicle_model_style_assignments_schema = PriceVehicleModelStyleAssignmentSchema(many=True)
