import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

// Dependencies
import { ApiHttpService } from '@dealer/services';

// Models
import { HttpApiResponseModel, Pagination } from '@dash/types';
import { VehicleOptionModel } from '../models/vehicle/vehicle-option.model';
import { map } from 'rxjs/operators';

@Injectable()
export class VehicleColorService {
  private vehicleColorsSource: BehaviorSubject<VehicleOptionModel[]> = new BehaviorSubject<VehicleOptionModel[]>([]);
  vehicleColors$: Observable<VehicleOptionModel[]> = this.vehicleColorsSource.asObservable();
  
  fetchFilterColors(yearModelId: string): Observable<Pagination<any>> {
    return this.fetchColors$(yearModelId).pipe(
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
        this.vehicleColorsSource.next(colors);
        return data.data;
      })
    )
  }

  fetchColors$(yearModelId: string): Observable<HttpApiResponseModel<Pagination<any>>> {
    return this.httpService.get<HttpApiResponseModel<Pagination<any>>>(`/vehicle_year_models/${yearModelId}/vehicle_model_styles`);
  }

  resetFilterColors(): void {
    this.vehicleColorsSource.next([]);
  }

  constructor(private httpService: ApiHttpService) { }
}