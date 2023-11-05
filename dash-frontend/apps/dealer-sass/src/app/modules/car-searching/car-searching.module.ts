import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ClipboardModule } from '@angular/cdk/clipboard';
import { AngularSvgIconModule } from 'angular-svg-icon';

// Module Dependencies
import { ScrollingModule } from '@angular/cdk/scrolling';
import { NzDropDownModule } from 'ng-zorro-antd/dropdown';
import { NzModalModule } from 'ng-zorro-antd/modal';
import { NzIconModule } from 'ng-zorro-antd/icon';
import { NzSkeletonModule } from 'ng-zorro-antd/skeleton';
import { NzSliderModule } from 'ng-zorro-antd/slider';
import { NzPaginationModule } from 'ng-zorro-antd/pagination';
import { NzToolTipModule } from 'ng-zorro-antd/tooltip';
import { NzCollapseModule } from 'ng-zorro-antd/collapse';
import { NzPopoverModule } from 'ng-zorro-antd/popover';
import { DashImageModule } from '@dash/common/dash-image/dash-image.module';
import { CarSearchingRoutingModule } from './car-searching-routing.module';

import { CarSearchingComponent } from './pages/car-searching/car-searching.component';
import { SearchingBannerComponent } from './parts/searching-banner/searching-banner.component';
import { SearchBarComponent } from './parts/search-bar/search-bar.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SearchingResultComponent } from './parts/searching-result/searching-result.component';
import { SearchingItemComponent } from './components/searching-item/searching-item.component';
import { SugesstionComponent } from './components/sugesstion/sugesstion.component';
import { PaginationComponent } from './components/pagination/pagination.component';
import { SearchingBarFilterComponent } from './components/searching-bar-filter/searching-bar-filter.component';
import { SelectBranchComponent } from './components/select-branch/select-branch.component';
import { SelectModelComponent } from './components/select-model/select-model.component';
import { SelectYearComponent } from './components/select-year/select-year.component';
import { SelectBodyTypeComponent } from './components/select-body-type/select-body-type.component';
import { SelectPriceRangeComponent } from './components/select-price-range/select-price-range.component';
import { SelectColorComponent } from './components/select-color/select-color.component';
import { SearchingFilterComponent } from './components/searching-filter/searching-filter.component';

// Services Dependency
import { VehicleBranchService } from './services/vehicle-branch.service';
import { VehicleModelService } from './services/vehicle-model.service';
import { VehicleYearModelService } from './services/vehicle-year-model.service';
import { VehicleColorService } from './services/vehicle-color.service';
import { VehicleBodyService } from './services/vehicle-body.service';
import { VehicleService } from './services/vehicle.service';
import { VehicleFilterMobileService } from './services/vehicle-filter-mobile.service';

@NgModule({
  declarations: [
    CarSearchingComponent,
    SearchingBannerComponent,
    SearchBarComponent,
    SearchingResultComponent,
    SearchingItemComponent,
    SugesstionComponent,
    PaginationComponent,
    SearchingBarFilterComponent,
    SelectBranchComponent,
    SelectModelComponent,
    SelectYearComponent,
    SelectBodyTypeComponent,
    SelectPriceRangeComponent,
    SelectColorComponent,
    SearchingFilterComponent,
  ],
  imports: [
    CommonModule,
    AngularSvgIconModule,
    ClipboardModule,
    CarSearchingRoutingModule,
    NzDropDownModule,
    NzModalModule,
    NzIconModule,
    NzSkeletonModule,
    NzSliderModule,
    FormsModule,
    NzPaginationModule,
    NzToolTipModule,
    ReactiveFormsModule,
    NzCollapseModule,
    DashImageModule,
    ScrollingModule,
    NzPopoverModule,
  ],
  providers: [
    VehicleBranchService,
    VehicleModelService,
    VehicleYearModelService,
    VehicleColorService,
    VehicleBodyService,
    VehicleService,
    VehicleFilterMobileService,
  ]
})
export class CarSearchingModule {
}
