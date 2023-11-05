import { VehicleDataModel, VehicleFilterBaseModel } from './vehicle-base.model';
import { VehicleGalleryModel } from '../common/gallery.model';
import { VehicleInfo } from '../common/vehicle-info.model';
import { VehicleEngineModel } from '../common/vehicle-engine.model';
import { VehicleTransmissionModel } from '../common/vehicle-transmission.model';
import { VehicleAttributeModel } from '../common/vehicle-attribute.model';
import { VehicleModel } from './vehicle.model';
import { VehicleDriveTrainModel } from '../common/vehicle-drive-train.model';
import { VehicleCategoryModel } from '../common/vehicle-category.model';

export interface VehicleYearModel extends VehicleFilterBaseModel, VehicleModel {
  categories: VehicleCategoryModel[],
  galleries: VehicleGalleryModel[],
  infos: VehicleInfo[],
  engines: VehicleEngineModel[],
  transmissions: VehicleTransmissionModel[],
  attributes: VehicleAttributeModel[],
  vehicle_model: VehicleDataModel,
  vehicle_model_id: number,
  year: number,
  drive_trains: VehicleDriveTrainModel[]
}
