import { VehicleFilterBaseModel } from '../vehicle/vehicle-base.model';
import { VehicleModel } from '../vehicle/vehicle.model';

export interface VehicleCategoryModel extends VehicleFilterBaseModel, VehicleModel {}
