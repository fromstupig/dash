import { VehicleBaseModel } from './vehicle-base.model';

export interface VehicleAttributeModel extends VehicleBaseModel {
  value: string;
  value_in_number?: number;
  vehicle_attribute?: any;
  vehicle_attribute_id?: number;
}
