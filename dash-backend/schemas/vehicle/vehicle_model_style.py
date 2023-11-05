from marshmallow import fields, EXCLUDE

from models.vehicle import VehicleModelStyle
from schemas.vehicle.price_vehicle_model_style_assignment import PriceVehicleModelStyleAssignmentSchema
from schemas.vehicle.vehicle_gallery_item import VehicleGalleryItemSchema
from schemas.vehicle.vehicle_option_item import VehicleOptionItemSchema
from schemas.vehicle.vehicle_feature import VehicleInfoSchema, VehicleEngineSchema, VehicleTransmissionSchema, \
    VehicleDriveTrainSchema, VehicleBodySchema
from schemas.vehicle.vehicle_attribute_value import VehicleAttributeValueSchema
from schemas.vehicle.vehicle_year_model import VehicleYearModelSchema
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema


class VehicleModelStyleSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema):
    __model__ = VehicleModelStyle

    class Meta:
        unknown = EXCLUDE

    name = fields.String(required=True)
    description = fields.String(required=True)

    vif_num = fields.Integer(dump_only=True)

    vehicle_year_model_id = fields.Integer()
    vehicle_year_model = fields.Nested(VehicleYearModelSchema, only=['name', 'description', 'vehicle_model'],
                                       dump_only=True)

    include_feature_description = fields.String()
    style_features = fields.List(fields.String(), default=[])
    standard_feature = fields.Dict()
    technical_feature = fields.Dict()
    consumer_info = fields.Dict()
    pricing_options = fields.Dict()

    base_MSRP = fields.Float()
    manufacture_code = fields.String()
    image_url = fields.String()

    body_id = fields.Integer()
    body = fields.Nested(VehicleBodySchema, many=False, dump_only=True)

    infos = fields.Nested(VehicleInfoSchema, many=True)
    engines = fields.Nested(VehicleEngineSchema, many=True)
    transmissions = fields.Nested(VehicleTransmissionSchema, many=True)
    drive_trains = fields.Nested(VehicleDriveTrainSchema, many=True)
    options = fields.Nested(VehicleOptionItemSchema, many=True)
    galleries = fields.Nested(VehicleGalleryItemSchema, many=True)

    current_price_assigment = fields.Nested(PriceVehicleModelStyleAssignmentSchema, many=True)


vehicle_model_style_schema = VehicleModelStyleSchema()
els_vehicle_model_style_schema = VehicleModelStyleSchema()
vehicle_model_styles_schema = VehicleModelStyleSchema(many=True)
