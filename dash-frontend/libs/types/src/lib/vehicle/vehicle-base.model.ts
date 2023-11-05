export interface VehicleBaseModel {
  id: number;
  modification_date: string;
  creation_date: string;
  is_active?: boolean;
}

export interface VehicleDataModel {
  name: string;
  description: string;
}
