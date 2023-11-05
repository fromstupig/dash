import { Component, OnInit, ChangeDetectionStrategy, ChangeDetectorRef, Input, Output, EventEmitter, OnDestroy } from '@angular/core';
import { SearchFilter } from '../../models/search-filter';
import { FilterValueModel } from '@dealer-modules/car-searching/models/emitter/filter.emitter-model';
import { SearchDataModel } from '@dealer-modules/car-searching/models/search-data';
import { RemoveFilterData } from '@dealer-modules/car-searching/models/filter';
import { Router, UrlSerializer, UrlTree, ActivatedRoute } from '@angular/router';
import { forkJoin, Observable, of, Subject } from 'rxjs';
import { mergeMap, take, takeUntil } from 'rxjs/operators';
import { FormBuilder, FormGroup } from '@angular/forms';
import { BreakpointService } from '@dealer-core/services/breakpoint.service';
import { VehicleBranchService } from '@dealer-modules/car-searching/services/vehicle-branch.service';
import { FilterEmmiterModel } from '@dash/types';
import { VehicleModelService } from '@dealer-modules/car-searching/services/vehicle-model.service';
import { VehicleYearModelService } from '@dealer-modules/car-searching/services/vehicle-year-model.service';
import { VehicleColorService } from '@dealer-modules/car-searching/services/vehicle-color.service';
import { VehicleBodyService } from '@dealer-modules/car-searching/services/vehicle-body.service';

enum Options {
  BRANCH = 'branch',
  MODEL = 'model',
  YEAR = 'year',
  BODY = 'body',
  PRICE = 'price',
  COLOR = 'color',
  FILTER = 'filter'
}

@Component({
  selector: 'dash-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SearchBarComponent implements OnInit, OnDestroy {
  @Input() total: number = 152;
  @Input('type') searchType: string = 'NEW';
  formSearch: FormGroup;
  modalName = '';
  sortType = 'Popular';
  isMobile$: Observable<boolean> = this.breakpointService.isMobileDevice;
  titles: {[key in Options]: string} = {
    branch: 'Select a brand',
    model: 'Select a model',
    year: 'Select year',
    body: 'Select body type',
    price: 'Price Range',
    color: 'Select color',
    filter: 'Filter',
  };
  data: SearchDataModel = {
    branch: of(Array.from(Array(15)).map(() => ({}))),
    model: of(Array.from(Array(1)).map(() => ({}))),
    year: of(Array.from(Array(2).map(() => ({})))),
    body: of(Array.from(Array(7).map(() => ({})))),
    price: of('2000-10000'),
    color: of(Array.from(Array(5).map(() => ({})))),
  }
  tooltip: any = {
    model: false,
    year: false,
    color: false
  }

  private onDestroy$: Subject<boolean> = new Subject<boolean>();

  ngOnInit(): void {
    this.initFormSearch();
    this.fetchFilterData();
    this.data = {
      branch: this.vehicleBranchService.vehicle$,
      model: this.vehicleModelService.vehicleModels$,
      year: this.vehicleYearModelService.vehicleYearModels$,
      body: this.vehicleBodyService.vehicleBodies$,
      color: this.vehicleColorService.vehicleColors$,
      price: this.data.price
    }
    this.mapParamsWithFilter(this.data);
  }

  private initFormSearch() {
    this.formSearch = this.fb.group({
      branch: [null],
      model: [null],
      year: [null],
      body: [null],
      color: [null],
      price: [null]
    });
    this.cdr.markForCheck();
  }

  private mapParamsWithFilter(data: any): void {
    this.activateRoute.queryParams.pipe(takeUntil(this.onDestroy$)).subscribe(params => {
      const result: SearchFilter = {};
      const paramsLength: Array<string> = Object.keys(params);
      this.modalName = '';
      if (paramsLength.length > 0) {
        paramsLength.map((key: string) => {
          if (data[key]) {
            if (key === 'price') {
              result[key] = {
                value: params[key],
                text: params[key],
                type: key
              }
              this.formSearch.patchValue(result);
            } else {
              (data[key] as Observable<any>).pipe(
                takeUntil(this.onDestroy$),
                take(2)
              ).subscribe((filtes: Array<any>) => {
                const filterItem = filtes.find((item) => item.id.toString() === params[key]);
                if (filterItem) {
                  result[key] = {
                    value: filterItem.id,
                    text: filterItem.name,
                    type: key
                  }
                  this.formSearch.patchValue(result);
                  this.cdr.markForCheck();
                }
              });
            }
          }
        });
      }
    });
  }

  ngOnDestroy(): void {
    this.onDestroy$.next(true);
    this.onDestroy$.complete();
  }

  handleCloseModal(): void {
    this.modalName = '';
    this.cdr.markForCheck();
  }

  openModal(modalName: string): void {
    if (modalName !== this.modalName) {
      switch (modalName) {
        case 'model': {
          if (this.formSearch.get('branch').value) {
            this.modalName = modalName;
          }
          break;
        }
        case 'year': {
          if (this.formSearch.get('model').value) {
            this.modalName = modalName;
          }
          break;
        }
        case 'color': {
          if (this.formSearch.get('year').value) {
            this.modalName = modalName;
          }
          break;
        }
        default: {
          this.modalName = modalName;
          break;
        }
      }
      this.cdr.markForCheck();
    }
  }

  onFilterChange(type: keyof SearchFilter, newFilter: FilterEmmiterModel): void {
    const value: FilterValueModel = {
      ...newFilter,
      type
    };
    this.onLoadFilterData(type, newFilter.value.toString())
    this.formSearch.patchValue({[type]: value});
    this.mergeFilterToQuery();
    this.modalName = '';
    this.cdr.markForCheck();
  }

  private onLoadFilterData(type: string, value: string): void {
    const filterValue: FilterValueModel | null = this.formSearch.get(type).value;
    if (value && ((filterValue && filterValue.value.toString() !== value) || !filterValue)) {
      switch (type) {
        case 'branch': {
          this.vehicleModelService.resetVehicleModelData$();
          this.vehicleYearModelService.resetVehicleYearModelsData$();
          this.vehicleModelService.fetchVehicleModels$(value).pipe(takeUntil(this.onDestroy$), take(1)).subscribe();
          break;
        }
        case 'model': {
          this.vehicleYearModelService.resetVehicleYearModelsData$();
          this.vehicleYearModelService.fetchListVehicleYearModels$(value).pipe(takeUntil(this.onDestroy$), take(1)).subscribe();
          break;
        }
        case 'year': {
          this.vehicleColorService.resetFilterColors();
          this.vehicleColorService.fetchFilterColors(value).pipe(takeUntil(this.onDestroy$), take(1)).subscribe();
          break;
        }
        default: {
          break;
        }
      }
    }
  }

  onRemoveFilter(data: RemoveFilterData): void {
    if (data.all) {
      this.formSearch.reset();
    } else {
      this.formSearch.patchValue({[data.filter.type]: null});
    }
    this.mergeFilterToQuery();
  }

  mergeFilterToQuery() {
    const params = {};
    const formValue = this.formSearch.value;
    Object.keys(formValue).map((key:  string) => {
      if (formValue[key] && formValue[key].value) {
        params[key] = formValue[key].value;
      }
    });
    const urlTree: UrlTree = this.router.createUrlTree([], { queryParams: params });
    this.router.navigateByUrl(this.serializer.serialize(urlTree));
  }

  onFilterMobileChange(filters: any): void {
    this.modalName = '';
    if (filters) {
      this.router.navigate(['searching'], { queryParams: filters, queryParamsHandling: 'merge' });
    }
  }

  private fetchFilterData() {
    this.activateRoute.queryParams.pipe(
      takeUntil(this.onDestroy$),
      take(1),
      mergeMap((params) => {
        const listQueries: Array<Observable<any>> = [
          this.vehicleBranchService.fetchVehicleList$(),
          this.vehicleBodyService.fetchListVehicleBody$(),
        ];
        if (params && params.branch) {
          listQueries.push(this.vehicleModelService.fetchVehicleModels$(params.branch));
        }
        if (params && params.model) {
          listQueries.push(this.vehicleYearModelService.fetchListVehicleYearModels$(params.model));
        }
        if (params && params.model && params.branch && params.year) {
          listQueries.push(this.vehicleColorService.fetchFilterColors(params.year));
        }
        return forkJoin(listQueries);
      })
    ).subscribe();
  }

  constructor(
    private readonly cdr: ChangeDetectorRef,
    private readonly router: Router,
    private readonly serializer: UrlSerializer,
    private readonly activateRoute: ActivatedRoute,
    private readonly fb: FormBuilder,
    private readonly breakpointService: BreakpointService,
    private readonly vehicleBranchService: VehicleBranchService,
    private readonly vehicleModelService: VehicleModelService,
    private readonly vehicleYearModelService: VehicleYearModelService,
    private readonly vehicleColorService: VehicleColorService,
    private readonly vehicleBodyService: VehicleBodyService,
  ) { }
}
