import { VehicleBaseModel } from '@dash/types';

export interface VehicleCustomAttributeModel extends VehicleBaseModel {
  vehicle_attribute_valueId?: number;
  vehicle_id?: number;
}
