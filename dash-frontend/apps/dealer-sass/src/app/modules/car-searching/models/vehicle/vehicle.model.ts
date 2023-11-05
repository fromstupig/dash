import {
  User,
  VehicleCustomAttributeModel,
  VehicleCustomOptionModel,
  VehicleGalleryModel,
  VehiclePriceAssignmentModel,
  VehicleBaseModel,
  VehicleHistoryModel,
  VehicleDataModel, VehicleBranchModel
} from '@dash/types';

export interface VehicleModel {
  name: string;
  description: string;
}

export interface VehicleSchema extends VehicleBaseModel {
  current_owner?: User;
  current_owner_id?: number;
  current_price_assigment?: VehiclePriceAssignmentModel;
  custom_attributes?: VehicleCustomAttributeModel[];
  custom_options?: VehicleCustomOptionModel[];
  description: string;
  galleries?: VehicleGalleryModel[];
  histories?: VehicleHistoryModel[];
  name: string;
  vehicle_brand?: VehicleBranchModel;
  vehicle_brand_id?: number;
  vehicle_model?: VehicleDataModel;
  vehicle_model_id?: number;
  vehicle_model_style?: any;
  vehicle_model_style_id?: number;
  avatar?: string;
  exColor?: VehicleCustomOptionModel;
}
