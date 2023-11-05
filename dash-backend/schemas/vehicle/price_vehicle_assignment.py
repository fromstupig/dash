from marshmallow import fields, EXCLUDE

from models.vehicle import PriceVehicleAssignment
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema, PriceAssignmentSchema


class PriceVehicleAssignmentSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PriceAssignmentSchema):
    __model__ = PriceVehicleAssignment

    class Meta:
        unknown = EXCLUDE

    vehicle_id = fields.Integer()


price_vehicle_assignment_schema = PriceVehicleAssignmentSchema()
price_vehicle_assignments_schema = PriceVehicleAssignmentSchema(many=True)
