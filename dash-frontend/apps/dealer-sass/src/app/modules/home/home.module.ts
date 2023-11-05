import { NgModule } from '@angular/core'
import { CommonModule } from '@angular/common'
import { GoogleMapsModule } from '@angular/google-maps'
import { HttpClientJsonpModule, HttpClientModule } from '@angular/common/http'

import { NzCollapseModule } from 'ng-zorro-antd/collapse'
import { NzModalModule } from 'ng-zorro-antd/modal'
import { NzSkeletonModule } from 'ng-zorro-antd/skeleton'

import { HomeRoutingModule } from './home-routing.module'
import { HomeComponent } from './pages/home/home.component'
import { BuildOwnCarModule } from '../../components/modals/build-own-car/build-own-car.module'

@NgModule({
  declarations: [HomeComponent],
  imports: [
    CommonModule,
    HomeRoutingModule,
    GoogleMapsModule,
    HttpClientModule,
    HttpClientJsonpModule,
    NzCollapseModule,
    NzModalModule,
    BuildOwnCarModule,
    NzSkeletonModule
  ]
})
export class HomeModule {}
