import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
// Dependencies
import { ApiHttpService } from '@dealer/services';

// Models
import { VehicleBranchModelData } from '@dealer-modules/car-searching/models/vehicle/vehicle-branch.model';
import { HttpApiResponseModel, Pagination } from '@dash/types';

@Injectable()
export class  VehicleBranchService {
  private vehiclesSource$: BehaviorSubject<VehicleBranchModelData[]> = new BehaviorSubject<VehicleBranchModelData[]>([]);
  public vehicle$: Observable<VehicleBranchModelData[]> = this.vehiclesSource$.asObservable();

  fetchVehicleList$(): Observable<Array<VehicleBranchModelData>> {
    return this.fetchBranches$().pipe(
      map((data: HttpApiResponseModel<Pagination<VehicleBranchModelData>>) => {
        this.setVehicleData(data.data.items);
        return data.data.items;
      }),
      catchError(() => {
        this.setVehicleData([]);
        return of([]);
      })
    );
  }

  fetchBranches$(): Observable<HttpApiResponseModel<Pagination<VehicleBranchModelData>>> {
    return this.httpService.get('/vehicle_brands');
  }

  private setVehicleData(data: Array<VehicleBranchModelData> = []): void {
    this.vehiclesSource$.next(data);
  }

  constructor(
    private httpService: ApiHttpService
  ) {}
}
