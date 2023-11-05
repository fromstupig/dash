import { VehicleBaseModel } from '@dash/types';

export interface VehicleOption {
  code: string;
  id: number;
  rgb1: string;
  rgb2?: string;
  shotin: number;
  simpletitle: string;
  title: string;
  vifnum: number;
}

export interface VehicleCustomOptionModel extends VehicleBaseModel {
  vehicle_id?: number;
  vehicle_option_item_id?: number;
  detail: VehicleOption;
  type: string;
}
