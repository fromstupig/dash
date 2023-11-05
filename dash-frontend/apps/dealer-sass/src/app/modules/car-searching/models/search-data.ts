import { Observable } from 'rxjs';
import { VehicleBranchModelData } from './vehicle/vehicle-branch.model';
import { VehicleModelModel } from './vehicle/vehicle-model.model';
import { VehicleYearModel } from '@dealer-modules/car-searching/models/vehicle/vehicle-year.model';
import { VehicleOptionModel } from './vehicle/vehicle-option.model';
import { VehicleBodyModel } from './vehicle/vehicle-body.nodel';

export interface ModelSearchDataModel {
  id: string;
  image: string;
  name: string;
}

export interface BodyTypeSearchDataModel {
  id: string;
  name: string;
  total: number;
}

export interface ColorSearchDataModel {
  id: string;
  name: string;
  total: number;
  color: string;
};

export interface SearchDataModel {
  branch: Observable<Array<Partial<VehicleBranchModelData>>>;
  model: Observable<Array<Partial<VehicleModelModel>>>;
  year: Observable<Array<Partial<VehicleYearModel>>>;
  body: Observable<Array<Partial<VehicleBodyModel>>>;
  price: Observable<string>;
  color: Observable<Array<Partial<VehicleOptionModel>>>;
}
