import { Injectable } from '@angular/core'
import {
  Resolve,
  ActivatedRouteSnapshot,
  RouterStateSnapshot
} from '@angular/router'
import { ApiHttpService } from '@dealer/services'

@Injectable({
  providedIn: 'root'
})
export class VehicleResolverService implements Resolve<any> {
  constructor(private apiService: ApiHttpService) {}

  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    return this.apiService.get(
      `/vehicle_model_styles/${route.paramMap.get('id')}`
    )
  }
}
