from schemas.dealer.dealer import DealerSchema
from schemas.dealer.dealer_scheduler import DealerSchedulerSchema
from schemas.request import ExceptionResponseSchema
from schemas.vehicle import *
from schemas.vehicle.vehicle_model_styles_search_schema import VehicleModelStylesSearchSchema
from schemas.vehicle.vehicle_status import vehicle_status_schema


def init_app(app, spec):
    spec.components.schema("ExceptionResponseSchema", schema=ExceptionResponseSchema)
    spec.components.schema("VehicleStatusSchema", schema=VehicleStatusSchema)
    spec.components.schema("VehicleCustomAttributeSchema", schema=VehicleCustomAttributeSchema)
    spec.components.schema("VehicleCustomOptionSchema", schema=VehicleCustomOptionSchema)
    spec.components.schema("VehicleGalleryItemSchema", schema=VehicleGalleryItemSchema)
    spec.components.schema("VehicleHistorySchema", schema=VehicleHistorySchema)
    spec.components.schema("PriceOptionAssignmentSchema", schema=PriceOptionAssignmentSchema)
    spec.components.schema("PriceVehicleAssignmentSchema", schema=PriceVehicleAssignmentSchema)
    spec.components.schema("PriceVehicleModelStyleAssignmentSchema", schema=PriceVehicleModelStyleAssignmentSchema)
    spec.components.schema("VehicleSchema", schema=VehicleSchema)
    spec.components.schema("VehicleAttributeSchema", schema=VehicleAttributeSchema)
    spec.components.schema("VehicleAttributeValueSchema", schema=VehicleAttributeValueSchema)
    spec.components.schema("VehicleBrandSchema", schema=VehicleBrandSchema)
    spec.components.schema("VehicleModelSchema", schema=VehicleModelSchema)
    spec.components.schema("VehicleYearModelSchema", schema=VehicleYearModelSchema)
    spec.components.schema("VehicleModelStyleSchema", schema=VehicleModelStyleSchema)
    spec.components.schema("VehicleModelStyleAttributeSchema", schema=VehicleModelStyleAttributeSchema)
    spec.components.schema("VehicleOptionItemSchema", schema=VehicleOptionItemSchema)
    spec.components.schema("VehicleYearModelAttributeSchema", schema=VehicleYearModelAttributeSchema)
    spec.components.schema("VehicleModelStylesSearchSchema", schema=VehicleModelStylesSearchSchema)
    spec.components.schema("DealerSchema", schema=DealerSchema)
    spec.components.schema("DealerSchedulerSchema", schema=DealerSchedulerSchema)
