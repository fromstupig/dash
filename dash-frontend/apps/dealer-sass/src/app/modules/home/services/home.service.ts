import { Injectable } from '@angular/core';
import { ApiHttpService } from '@dealer/services';
import { HttpApiResponseModel } from '@dash/types';
import { VehiclePagination } from '@dealer-modules/home/models';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  constructor(private apiService: ApiHttpService) { }

  public getVehicleModel(params?): Observable<VehiclePagination> {
    if (!params) {
      params = {
        direction: 'asc',
        is_active: 'true',
        limit: '20',
        offset: '0',
        sort: 'true'
      };
    }
    return this.apiService.get<HttpApiResponseModel<VehiclePagination>>('/vehicle_models', params).pipe(
      map((data: HttpApiResponseModel<VehiclePagination>) => data.data)
    );
  }
}




