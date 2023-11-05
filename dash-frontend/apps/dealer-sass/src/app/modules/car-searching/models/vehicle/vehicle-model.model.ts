import { VehicleBranchBaseModel } from './vehicle-branch.model';
import { VehicleFilterBaseModel } from './vehicle-base.model';
import { VehicleGalleryModel } from '../common/gallery.model';

export interface VehicleModelModel
  extends VehicleBranchBaseModel,
    VehicleFilterBaseModel {
  galleries: VehicleGalleryModel[];
  vehicle_brand_id: number;
  vehicle_brand: VehicleBranchBaseModel;
}
