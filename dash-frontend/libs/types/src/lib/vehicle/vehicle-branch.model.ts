import { VehicleGalleryModel } from './vehicle-gallery.model';

export interface VehicleBranchModel {
  name: string;
  description: string;
}

export interface VehicleBranchModelData extends VehicleBranchModel {
  creation_date: string;
  galleries: VehicleGalleryModel[];
  id: number;
  modification_date: string;
}
