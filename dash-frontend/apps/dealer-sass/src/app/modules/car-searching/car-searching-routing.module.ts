import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CarSearchingComponent } from './pages/car-searching/car-searching.component';

const routes: Routes = [
  {
    path: '',
    component: CarSearchingComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CarSearchingRoutingModule { }
