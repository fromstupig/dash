import { VehicleBaseModel } from '@dash/types';

export interface VehicleGalleryModel extends VehicleBaseModel {
  asset_path: string;
    order?: number;
    type: VehicleGalleryItem.TypeEnum;
}

export namespace VehicleGalleryItem {
  export type TypeEnum = 'COVER' | 'INTERIOR' | 'INTERIOR_COLOR' | 'EXTERIOR' | 'EXTERIOR_COLOR' | 'BRAND_LOGO' | 'MODEL_AVATAR' | 'YEAR_MODEL_AVATAR' | 'VIDEO_INTRODUCTION' | 'MODEL_STYLE_AVATAR' | 'OPTION_ITEM_AVATAR' | 'VEHICLE_AVATAR' | 'OTHERS';
  export const TypeEnum = {
    COVER: 'COVER' as TypeEnum,
    INTERIOR: 'INTERIOR' as TypeEnum,
    INTERIORCOLOR: 'INTERIOR_COLOR' as TypeEnum,
    EXTERIOR: 'EXTERIOR' as TypeEnum,
    EXTERIORCOLOR: 'EXTERIOR_COLOR' as TypeEnum,
    BRANDLOGO: 'BRAND_LOGO' as TypeEnum,
    MODELAVATAR: 'MODEL_AVATAR' as TypeEnum,
    YEARMODELAVATAR: 'YEAR_MODEL_AVATAR' as TypeEnum,
    VIDEOINTRODUCTION: 'VIDEO_INTRODUCTION' as TypeEnum,
    MODELSTYLEAVATAR: 'MODEL_STYLE_AVATAR' as TypeEnum,
    OPTIONITEMAVATAR: 'OPTION_ITEM_AVATAR' as TypeEnum,
    VEHICLEAVATAR: 'VEHICLE_AVATAR' as TypeEnum,
    OTHERS: 'OTHERS' as TypeEnum
  };
}
