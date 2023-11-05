import { VehicleBaseModel } from '@dash/types';

export interface VehicleStatusModel extends VehicleBaseModel {
  checked_date: Date;
  mileage?: number;
  note?: string;
  vehicle_history_id?: number;
}
