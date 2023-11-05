from marshmallow import fields, EXCLUDE

from models.vehicle import VehicleYearModel
from schemas.vehicle.vehicle_gallery_item import VehicleGalleryItemSchema
from schemas.vehicle.vehicle_attribute_value import VehicleAttributeValueSchema
from schemas.vehicle.vehicle_feature import VehicleInfoSchema, VehicleEngineSchema, VehicleTransmissionSchema, \
    VehicleDriveTrainSchema, VehicleCategorySchema
from schemas.vehicle.vehicle_model import VehicleModelSchema
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema


class VehicleYearModelSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    __model__ = VehicleYearModel

    class Meta:
        unknown = EXCLUDE

    name = fields.String(required=True)
    description = fields.String(required=True)
    year = fields.Integer()

    vehicle_model_id = fields.Integer()
    vehicle_model = fields.Nested(VehicleModelSchema, only=['name', 'description', 'vehicle_brand'], dump_only=True)

    attributes = fields.Nested(VehicleAttributeValueSchema, many=True, dump_only=True)

    infos = fields.Nested(VehicleInfoSchema, many=True)
    engines = fields.Nested(VehicleEngineSchema, many=True)
    transmissions = fields.Nested(VehicleTransmissionSchema, many=True)

    drive_trains = fields.Nested(VehicleDriveTrainSchema, many=True)
    categories = fields.Nested(VehicleCategorySchema, many=True)

    galleries = fields.Nested(VehicleGalleryItemSchema, many=True)

vehicle_year_model_schema = VehicleYearModelSchema()
vehicle_year_models_schema = VehicleYearModelSchema(many=True)
