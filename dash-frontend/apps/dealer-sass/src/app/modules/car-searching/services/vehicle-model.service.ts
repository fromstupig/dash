import { Injectable } from '@angular/core';
import { ApiHttpService } from '@dealer/services';
import { BehaviorSubject, Observable } from 'rxjs';
import { VehicleModelModel } from '@dealer-modules/car-searching/models/vehicle/vehicle-model.model';
import { map, tap } from 'rxjs/operators';
import { HttpApiResponseModel, Pagination } from '@dash/types';

@Injectable()
export class VehicleModelService {
  private vehicleModelsSource: BehaviorSubject<VehicleModelModel[]> = new BehaviorSubject<VehicleModelModel[]>([]);
  vehicleModels$: Observable<VehicleModelModel[]> = this.vehicleModelsSource.asObservable();

  fetchVehicleModels$(vehicleBranchId: string): Observable<Pagination<VehicleModelModel>> {
    return this.fetchModels$(vehicleBranchId).pipe(
      map((data: HttpApiResponseModel<Pagination<VehicleModelModel>>) => {
        this.vehicleModelsSource.next(data.data.items);
        return data.data;
      }))
  }

  fetchModels$(vehicleBranchId: string): Observable<HttpApiResponseModel<Pagination<VehicleModelModel>>> {
    return this.httpService.get<HttpApiResponseModel<Pagination<VehicleModelModel>>>(`/vehicle_brands/${vehicleBranchId}/vehicle_models`);
  }

  resetVehicleModelData$(): void {
    this.vehicleModelsSource.next([]);
  }

  constructor(
    private readonly httpService: ApiHttpService
  ) { }
}
