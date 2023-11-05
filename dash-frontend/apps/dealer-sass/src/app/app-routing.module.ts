import { NgModule } from '@angular/core'
import { Routes, RouterModule } from '@angular/router'
import { VehicleResolverService } from '@dealer-modules/vehicle/vehicle-resolver.service'

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: '/home' },
  {
    path: 'home',
    loadChildren: () =>
      import('@dealer-modules/home/home.module').then((m) => m.HomeModule)
  },
  {
    path: 'board',
    loadChildren: () =>
      import('@dealer-modules/board/board.module').then((m) => m.BoardModule)
  },
  {
    path: 'searching',
    loadChildren: () =>
      import('@dealer-modules/car-searching/car-searching.module').then(
        (m) => m.CarSearchingModule
      )
  },
  {
    path: 'vehicle/:id',
    loadChildren: () =>
      import('@dealer-modules/vehicle/vehicle.module').then(
        (m) => m.VehicleModule
      ),
    resolve: {
      vehicle: VehicleResolverService
    }
  }
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
