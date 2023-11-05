import { Injectable } from '@angular/core';
import { ApiHttpService } from '@dealer/services';
import { HttpApiResponseModel, Pagination } from '@dash/types';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { VehicleYearModel } from '../models/vehicle/vehicle-year.model';

@Injectable()
export class VehicleYearModelService {
  private vehicleYearModelsSource: BehaviorSubject<VehicleYearModel[]> = new BehaviorSubject<VehicleYearModel[]>([]);
  vehicleYearModels$: Observable<VehicleYearModel[]> = this.vehicleYearModelsSource.asObservable();

  fetchListVehicleYearModels$(vehicleModelId: string): Observable<Pagination<VehicleYearModel>> {
    return this.fetchYears$(vehicleModelId).pipe(
      map((data: HttpApiResponseModel<Pagination<VehicleYearModel>>) => {
        this.vehicleYearModelsSource.next(data.data.items);
        return data.data;
      })
    )
  }

  fetchYears$(vehicleModelId: string): Observable<HttpApiResponseModel<Pagination<VehicleYearModel>>> {
    return this.httpService.get<HttpApiResponseModel<Pagination<VehicleYearModel>>>(`/vehicle_models/${vehicleModelId}/vehicle_year_models`);
  }

  resetVehicleYearModelsData$(): void {
    this.vehicleYearModelsSource.next([]);
  }

  constructor(
    private httpService: ApiHttpService
  ) { }
}
