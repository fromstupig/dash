import { VehicleFilterBaseModel } from './vehicle-base.model';
import { VehicleGalleryModel } from '../common/gallery.model';

export interface VehicleOptionModel extends VehicleFilterBaseModel { 
  current_price_assigment?: Array<any>;
  description: string;
  detail: any;
  galleries: VehicleGalleryModel[];
  is_popular: boolean;
  type: VehicleOptionItemSchema.TypeEnum;
}
export namespace VehicleOptionItemSchema {
  export type TypeEnum = 'INTERIOR_COLOR' | 'EXTERIOR_COLOR' | 'PACKAGE' | 'OPTION' | 'OTHERS';
  export const TypeEnum = {
      INTERIORCOLOR: 'INTERIOR_COLOR' as TypeEnum,
      EXTERIORCOLOR: 'EXTERIOR_COLOR' as TypeEnum,
      PACKAGE: 'PACKAGE' as TypeEnum,
      OPTION: 'OPTION' as TypeEnum,
      OTHERS: 'OTHERS' as TypeEnum
  };
}
