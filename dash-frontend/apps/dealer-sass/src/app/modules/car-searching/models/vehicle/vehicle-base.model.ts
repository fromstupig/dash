import { VehicleModel } from '@dealer-modules/car-searching/models/vehicle/vehicle.model';

export interface VehicleFilterBaseModel {
  id: number;
  modification_date: string;
  creation_date: string;
  is_active?: boolean;
}

export interface VehicleDataModel {
  description: string;
  name: string;
  vehicle_brand: VehicleModel;
}
