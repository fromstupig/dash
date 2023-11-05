import { VehicleFilterBaseModel } from '../vehicle/vehicle-base.model';

export interface VehicleEngineModel extends VehicleFilterBaseModel {
  horse_power?: number;
  is_active?: boolean;
  label?: string;
  torque?: number;
  type: VehicleEngine.TypeEnum;
}

export namespace VehicleEngine {
  export type TypeEnum = 'OTHERS' | 'GAS' | 'DIESEL' | 'ELECTRIC';
  export const TypeEnum = {
    OTHERS: 'OTHERS' as TypeEnum,
    GAS: 'GAS' as TypeEnum,
    DIESEL: 'DIESEL' as TypeEnum,
    ELECTRIC: 'ELECTRIC' as TypeEnum
  };
}
