import { VehicleBaseModel } from './vehicle-base.model';

export interface VehiclePriceAssignmentModel extends VehicleBaseModel {
  end_date?: Date;
  region_id?: number;
  start_date?: Date;
  value_in_cent?: number;
  vehicle_id?: number;
}
