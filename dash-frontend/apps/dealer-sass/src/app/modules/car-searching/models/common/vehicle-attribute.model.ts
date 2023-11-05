import { VehicleFilterBaseModel } from '../vehicle/vehicle-base.model';

export interface VehicleAttributeModel extends VehicleFilterBaseModel {
  value: string;
  value_in_number?: number;
  vehicle_attribute?: any;
  vehicle_attribute_id?: number;
}
