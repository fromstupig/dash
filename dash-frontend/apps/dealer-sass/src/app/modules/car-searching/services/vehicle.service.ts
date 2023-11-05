import { Injectable } from '@angular/core';
import { HttpApiResponseModel, Pagination, VehicleCustomOptionModel } from '@dash/types';
import { ApiHttpService } from '@dealer/services';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { VehicleSchema } from '../models/vehicle/vehicle.model';

@Injectable()
export class VehicleService {
  searchCars(filter: any): Observable<Pagination<VehicleSchema>> {
    return this.httpService.get<HttpApiResponseModel<Pagination<VehicleSchema>>>(`/vehicles/_search`, filter).pipe(
      map((data: HttpApiResponseModel<Pagination<VehicleSchema>>) => {
        const vehicles: Array<VehicleSchema> = data.data.items.map((vehicle: VehicleSchema) => {
          const color: VehicleCustomOptionModel = vehicle.custom_options.find((customOptions: VehicleCustomOptionModel) => customOptions.type === "EXTERIOR_COLOR");
          const galleryItem: any = vehicle.vehicle_model_style.galleries.find((item: any) => {
            return item && item.type === "EXTERIOR_COLOR" && item.asset_path && item.asset_path.includes(color.detail.code);
          });
          return {
            ...vehicle,
            avatar: galleryItem ? galleryItem.asset_path : '',
            exColor: color,
          }
        });
        return {
          total: data.data.total,
          items: vehicles,
        }
      })
    )
  }

  constructor(private httpService: ApiHttpService) {
  }
}
