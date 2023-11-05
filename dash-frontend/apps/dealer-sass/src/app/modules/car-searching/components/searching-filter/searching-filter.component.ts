import { ChangeDetectionStrategy, ChangeDetectorRef, Component, EventEmitter, Input, OnChanges, OnDestroy, OnInit, Output, SimpleChanges } from '@angular/core';
import { SearchDataModel } from '@dealer-modules/car-searching/models/search-data';
import { ActivatedRoute } from '@angular/router';
import { Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';
import { Dictionary } from '@dash/types';
import { FormBuilder, FormGroup } from '@angular/forms';
import { VehicleFilterMobileService } from '@dealer-modules/car-searching/services/vehicle-filter-mobile.service';

@Component({
  selector: 'dash-searching-filter',
  templateUrl: './searching-filter.component.html',
  styleUrls: ['./searching-filter.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SearchingFilterComponent implements OnInit, OnChanges, OnDestroy {
  @Input() data: SearchDataModel;
  @Input() formValue: any;
  @Output() onFilterChange: EventEmitter<any> = new EventEmitter<any>();
  queryParams: Dictionary = {};
  formFilter: FormGroup;
  filterData: SearchDataModel;
  panels = {
    branch: false,
    model: false,
    body: false,
    color: false,
    price: true,
    year: false,
  }
  private onDestroy$: Subject<boolean> = new Subject<boolean>();

  ngOnInit(): void {
    this.initFormFilter();
    this.route.queryParams.pipe(takeUntil(this.onDestroy$)).subscribe((queryParams: Dictionary<string>) => {
      this.queryParams = queryParams;
      this.cdr.markForCheck();
    });
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes && changes.data) {
      this.filterData = this.data;
    }
  }

  ngOnDestroy(): void {
    this.onDestroy$.next(true);
    this.onDestroy$.complete();
  }

  onFilterSelected(key: string, value: any): void {
    if (this.formFilter.get(key).value !== value) {
      this.panels[key] = false;
      this.formFilter.patchValue({ [key]: { type: key, text: value.name, value: value.id } });
      switch (key) {
        case 'branch':
          this.vehicleFilterMobileService.fetchVehicleModels$(value.id).pipe(takeUntil(this.onDestroy$)).subscribe();
          this.filterData.model = this.vehicleFilterMobileService.vehicleModels;
          break;
        case 'model': {
          this.vehicleFilterMobileService.fetchVehicleYears$(value.id).pipe(takeUntil(this.onDestroy$)).subscribe();
          this.filterData.year = this.vehicleFilterMobileService.vehicleYears;
          break;
        }
        case 'year': {
          this.vehicleFilterMobileService.fetchVehicleColors$(value.id).pipe(takeUntil(this.onDestroy$)).subscribe();
          this.filterData.color = this.vehicleFilterMobileService.vehicleColors;
          break;
        }
        default:
          break;
      }
    }
  }

  onSubmitFilter(): void {
    const formFilterValue: any = this.formFilter.value;
    const filters = Object.keys(formFilterValue).reduce((filterObject, currentFilter) => {
      if (formFilterValue[currentFilter]) {
        filterObject[currentFilter] = formFilterValue[currentFilter].value;
      }
      return filterObject;
    }, {});
    this.onFilterChange.emit(filters);
  }

  onResetFilter(): void {
    this.onFilterChange.emit(null);
  }

  closeFilter(name: string, status: any) {
    this.panels[name] = true;
  }

  onPriceFilterChange(priceValue: any) {
    this.formFilter.patchValue({ price: { ...priceValue, type: 'price' } });
  }

  private initFormFilter(): void {
    this.formFilter = this.fb.group({
      body: [null],
      branch: [null],
      color: [null],
      model: [null],
      price: [null],
      year: [null],
    });
    if (this.formValue) {
      this.formFilter.patchValue(this.formValue);
    }
  }

  constructor(
    private readonly route: ActivatedRoute,
    private readonly cdr: ChangeDetectorRef,
    private readonly fb: FormBuilder,
    private readonly vehicleFilterMobileService: VehicleFilterMobileService,
  ) { }
}
