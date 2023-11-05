import { User, VehicleBaseModel, VehicleStatusModel } from '@dash/types';

export interface VehicleHistoryModel extends VehicleBaseModel {
  owner?: User;
  owner_id?: number;
  purchased_date: Date;
  statuses?: VehicleStatusModel[];
  vehicle_id?: number;
}
