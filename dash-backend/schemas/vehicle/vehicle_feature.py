from marshmallow import fields, EXCLUDE
from marshmallow_enum import EnumField

from models.vehicle.vehicle_feature import VehicleEngine, VehicleDriveTrain, VehicleCategory, VehicleBody, EngineType, \
    VehicleTransmission, TransmissionType, VehicleWarranty, VehicleInfo
from schemas.base import IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema


class VehicleDriveTrainSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema):
    __model__ = VehicleDriveTrain

    class Meta:
        unknown = EXCLUDE

    name = fields.String(required=True)
    description = fields.String(required=True)


vehicle_drive_train_schema = VehicleDriveTrainSchema()
vehicle_drive_trains_schema = VehicleDriveTrainSchema(many=True)


class VehicleCategorySchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema):
    __model__ = VehicleCategory

    class Meta:
        unknown = EXCLUDE

    name = fields.String(required=True)
    description = fields.String(required=True)


vehicle_category_schema = VehicleCategorySchema()
vehicle_categories_schema = VehicleCategorySchema(many=True)


class VehicleBodySchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema):
    __model__ = VehicleBody

    class Meta:
        unknown = EXCLUDE

    name = fields.String(required=True)
    description = fields.String(required=True)


vehicle_bodyschema = VehicleCategorySchema()
vehicle_bodies_schema = VehicleCategorySchema(many=True)


class VehicleEngineSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema):
    __model__ = VehicleEngine

    class Meta:
        unknown = EXCLUDE

    label = fields.String()
    horse_power = fields.Integer()
    torque = fields.Integer()
    type = EnumField(EngineType, required=True)


vehicle_engine_schema = VehicleEngineSchema()
vehicle_engines_schema = VehicleEngineSchema(many=True)


class VehicleTransmissionSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema):
    __model__ = VehicleTransmission

    class Meta:
        unknown = EXCLUDE

    label = fields.String()
    speeds = fields.Integer()
    type = EnumField(TransmissionType, required=True)


vehicle_transmission_schema = VehicleTransmissionSchema()
vehicle_transmissions_schema = VehicleTransmissionSchema(many=True)


class VehicleWarrantySchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema):
    __model__ = VehicleWarranty

    class Meta:
        unknown = EXCLUDE

    comprehensive = fields.String()
    power_train = fields.String()
    anti_corrosion = fields.String()
    paint = fields.String()
    roadside_assistance = fields.String()


vehicle_warranty_schema = VehicleTransmissionSchema()
vehicle_warranties_schema = VehicleTransmissionSchema(many=True)


class VehicleInfoSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema):
    __model__ = VehicleInfo

    class Meta:
        unknown = EXCLUDE

    description = fields.String()

    city_mpg = fields.Integer()
    combined_mpg = fields.Integer()
    highway_mpg = fields.Integer()

    safety_rate = fields.Integer()

    doors = fields.Integer()
    seats = fields.Integer()

    vehicle_warranty = fields.Nested(VehicleWarrantySchema, many=False)


vehicle_info_schema = VehicleInfoSchema()
vehicle_infos_schema = VehicleInfoSchema(many=True)
