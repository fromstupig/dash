import { NgModule } from '@angular/core'
import { SharedModule } from '@dealer-shared/shared.module'

import { AngularSvgIconModule } from 'angular-svg-icon'
import { NzSliderModule } from 'ng-zorro-antd/slider'
import { NzRadioModule } from 'ng-zorro-antd/radio'
import { NzModalModule } from 'ng-zorro-antd/modal'
import { NzTabsModule } from 'ng-zorro-antd/tabs'
import { NzDividerModule } from 'ng-zorro-antd/divider'

import { VehicleRoutingModule } from './vehicle-routing.module'
import { VehicleDetailComponent } from './pages/vehicle-detail/vehicle-detail.component'
import { VehicleImageSliderComponent } from './components/vehicle-image-slider/vehicle-image-slider.component'
import { VehicleDeatailHeaderComponent } from './components/vehicle-deatail-header/vehicle-deatail-header.component'
import { VehicleFeatureColComponent } from './components/vehicle-feature-col/vehicle-feature-col.component'
import { PaymentService } from './payment.service';
import { AuthModule } from '../auth/auth.module';
import { VehicleLeasePaymentComponent } from './components/payments/lease-payment.component';
import { VehicleFinancePaymentComponent } from './components/payments/finance-payment.component';
import { VehicleCashPaymentComponent } from './components/payments/cash-payment.component';
import { CommonModule } from '@angular/common';
import { NzSpinModule } from 'ng-zorro-antd/spin';
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    VehicleDetailComponent,
    VehicleImageSliderComponent,
    VehicleDeatailHeaderComponent,
    VehicleFeatureColComponent,
    VehicleLeasePaymentComponent,
    VehicleFinancePaymentComponent,
    VehicleCashPaymentComponent,
  ],
  imports: [
    VehicleRoutingModule,
    SharedModule,
    CommonModule,
    AuthModule,
    AngularSvgIconModule.forRoot(),
    NzSliderModule,
    NzRadioModule,
    NzModalModule,
    NzTabsModule,
    NzDividerModule,
    NzSpinModule,
    ReactiveFormsModule
  ],
  providers: [PaymentService]
})
export class VehicleModule {}
