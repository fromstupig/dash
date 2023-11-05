import { VehicleGalleryModel } from '../common/gallery.model';

export interface VehicleBranchBaseModel {
  name: string;
  description: string;
}

export interface VehicleBranchModelData extends VehicleBranchBaseModel {
  creation_date: string;
  galleries: VehicleGalleryModel[];
  id: number;
  modification_date: string;
}
