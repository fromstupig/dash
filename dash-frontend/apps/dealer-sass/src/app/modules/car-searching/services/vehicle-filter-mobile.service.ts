import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, of } from 'rxjs';
import { VehicleBranchModelData } from '@dealer-modules/car-searching/models/vehicle/vehicle-branch.model';
import { VehicleModelModel } from '@dealer-modules/car-searching/models/vehicle/vehicle-model.model';
import { VehicleYearModel } from '@dealer-modules/car-searching/models/vehicle/vehicle-year.model';
import { VehicleOptionModel } from '@dealer-modules/car-searching/models/vehicle/vehicle-option.model';
import { catchError, map } from 'rxjs/operators';
import { HttpApiResponseModel, Pagination } from '@dash/types';
import { VehicleModelService } from './vehicle-model.service';
import { VehicleBranchService } from './vehicle-branch.service';
import { VehicleYearModelService } from './vehicle-year-model.service';
import { VehicleColorService } from './vehicle-color.service';

@Injectable()
export class VehicleFilterMobileService {
  private vehicleBranchSource$: BehaviorSubject<VehicleBranchModelData[]> = new BehaviorSubject<VehicleBranchModelData[]>([]);
  vehicleBranches: Observable<VehicleBranchModelData[]> = this.vehicleBranchSource$.asObservable();
  private vehicleModelSource$: BehaviorSubject<VehicleModelModel[]> = new BehaviorSubject<VehicleModelModel[]>([]);
  vehicleModels: Observable<VehicleModelModel[]> = this.vehicleModelSource$.asObservable();
  private vehicleYearSource$: BehaviorSubject<VehicleYearModel[]> = new BehaviorSubject<VehicleYearModel[]>([]);
  vehicleYears: Observable<VehicleYearModel[]> = this.vehicleYearSource$.asObservable();
  private vehicleColorSource$: BehaviorSubject<VehicleOptionModel[]> = new BehaviorSubject<VehicleOptionModel[]>([]);
  vehicleColors: Observable<VehicleOptionModel[]> = this.vehicleColorSource$.asObservable();

  fetchVehicleBranch$(): Observable<Array<VehicleBranchModelData>> {
    return this.vehicleBranchService.fetchBranches$().pipe(
      map((data: HttpApiResponseModel<Pagination<VehicleBranchModelData>>) => {
        this.vehicleBranchSource$.next(data.data.items);
        return data.data.items;
      }),
      catchError(() => {
        this.vehicleBranchSource$.next([]);
        return of([]);
      })
    );
  }

  fetchVehicleModels$(vehicleBranchId: string): Observable<Pagination<VehicleModelModel>> {
    return this.vehicleModelService.fetchModels$(vehicleBranchId).pipe(
      map((data: HttpApiResponseModel<Pagination<VehicleModelModel>>) => {
        this.vehicleModelSource$.next(data.data.items);
        return data.data;
      }))
  }

  fetchVehicleYears$(vehicleModelId: string): Observable<Pagination<VehicleYearModel>> {
    return this.vehicleYearService.fetchYears$(vehicleModelId).pipe(
      map((data: HttpApiResponseModel<Pagination<VehicleYearModel>>) => {
        this.vehicleYearSource$.next(data.data.items);
        return data.data;
      })
    )
  }

  fetchVehicleColors$(yearModelId: string): Observable<Pagination<VehicleOptionModel>> {
    return this.vehicleColorService.fetchColors$(yearModelId).pipe(
      map((data: HttpApiResponseModel<Pagination<any>>) => {
        const listColors = {};
        const colors: VehicleOptionModel[] = data.data.items.reduce((result: VehicleOptionModel[], item: any) => {
          const list = [];
          for (let i = 0; i < item.options.length; i++) {
            if (item.options[i].detail.code && !listColors[item.options[i].detail.code]) {
              listColors[item.options[i].detail.code] = true;
              list.push({
                ...item.options[i],
                name: item.options[i].detail.title,
              })
            }
          }
          return list.concat(result);
        }, [])
        this.vehicleColorSource$.next(colors);
        return data.data;
      })
    )
  }

  constructor(
    private readonly vehicleBranchService: VehicleBranchService,
    private readonly vehicleModelService: VehicleModelService,
    private readonly vehicleYearService: VehicleYearModelService,
    private readonly vehicleColorService: VehicleColorService,
  ) {}
}