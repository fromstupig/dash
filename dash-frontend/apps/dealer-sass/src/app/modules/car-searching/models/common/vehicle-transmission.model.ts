import { VehicleFilterBaseModel } from '../vehicle/vehicle-base.model';

export interface VehicleTransmissionModel extends VehicleFilterBaseModel {
  label?: string;
  speeds?: number;
  type: VehicleTransmission.TypeEnum;
}
export namespace VehicleTransmission {
  export type TypeEnum = 'OTHERS' | 'AUTOMATIC' | 'MANUAL';
  export const TypeEnum = {
    OTHERS: 'OTHERS' as TypeEnum,
    AUTOMATIC: 'AUTOMATIC' as TypeEnum,
    MANUAL: 'MANUAL' as TypeEnum
  };
}
