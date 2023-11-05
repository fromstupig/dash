import { VehicleFilterBaseModel } from './vehicle-base.model';

export interface VehicleBodyModel extends VehicleFilterBaseModel {
  description: string;
  name: string;
}
