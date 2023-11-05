import { VehicleFilterBaseModel } from '../vehicle/vehicle-base.model';

export interface VehicleWarranty extends VehicleFilterBaseModel {
  anti_corrosion?: string;
  comprehensive?: string;
  is_active?: boolean;
  paint?: string;
  power_train?: string;
  roadside_assistance?: string;
}

export interface VehicleInfo extends VehicleFilterBaseModel {
  city_mpg?: number;
  combined_mpg?: number;
  description?: string;
  doors?: number;
  highwayMpg?: number;
  isActive?: boolean;
  safetyRate?: number;
  seats?: number;
  vehicleWarranty?: VehicleWarranty;
}
