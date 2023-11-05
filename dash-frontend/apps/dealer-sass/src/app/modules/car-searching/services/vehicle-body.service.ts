import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

// Service Dependencies
import { ApiHttpService } from '@dealer/services';

// Models
import { VehicleBodyModel } from '@dealer-modules/car-searching/models/vehicle/vehicle-body.nodel';
import { HttpApiResponseModel, Pagination } from '@dash/types';

@Injectable()
export class VehicleBodyService {
  private vehicleBodiesSource: BehaviorSubject<VehicleBodyModel[]> = new BehaviorSubject<VehicleBodyModel[]>([]);
  vehicleBodies$: Observable<VehicleBodyModel[]> = this.vehicleBodiesSource.asObservable();

  fetchListVehicleBody$(): Observable<Pagination<VehicleBodyModel>> {
    return this.httpService.get<HttpApiResponseModel<Pagination<VehicleBodyModel>>>(`/vehicles_features/bodies`).pipe(
      map((data: HttpApiResponseModel<Pagination<VehicleBodyModel>>) => {
        this.vehicleBodiesSource.next(data.data.items);
        return data.data;
      })
    )
  }

  constructor(
    private httpService: ApiHttpService
  ) { }
}