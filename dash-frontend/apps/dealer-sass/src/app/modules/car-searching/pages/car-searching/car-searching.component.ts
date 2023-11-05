import { Component, OnInit, ChangeDetectionStrategy, OnDestroy, ChangeDetectorRef } from '@angular/core';
import { Dictionary, Pagination } from '@dash/types';
import { of, Subject } from 'rxjs';
import { VehicleSchema } from '@dealer-modules/car-searching/models/vehicle/vehicle.model';
import { ActivatedRoute, Router } from '@angular/router';
import { VehicleService } from '@dealer-modules/car-searching/services/vehicle.service';
import { catchError, distinctUntilChanged, mergeMap, takeUntil } from 'rxjs/operators';
import { SearchFilterMapper } from '@dealer-modules/car-searching/mapper/search-filter.mapper';
import { HttpErrorResponse } from '@angular/common/http';
import { DEFAULT_PAGE_SIZE } from '@dealer-modules/car-searching/constants/pagination.constant';

const DEFAULT_CARS: Pagination<VehicleSchema> = { total: 0, items: Array.from(Array(7)).map(() => ({ name: '', description: '' } as VehicleSchema)) };

@Component({
  selector: 'dash-car-searching',
  templateUrl: './car-searching.component.html',
  styleUrls: ['./car-searching.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class CarSearchingComponent implements OnInit, OnDestroy {
  type: string = 'NEW';
  cars: Pagination<VehicleSchema> = DEFAULT_CARS;
  page: number = 1;
  private onDestroy$: Subject<boolean> = new Subject<boolean>();

  ngOnInit(): void {
    this.route.queryParams.pipe(
      takeUntil(this.onDestroy$),
      distinctUntilChanged(),
      mergeMap((params) => {
        this.cars = DEFAULT_CARS;
        const queryParams: Dictionary = Object.keys(params).reduce((result: Dictionary, currentKey: string) => {
          if (SearchFilterMapper[currentKey]) {
            result[SearchFilterMapper[currentKey]] = params[currentKey];
          }
          if (currentKey === 'price') {
            if (params[currentKey] === '>20000') {
              result['filter_price_from'] = 20000;
            } else {
              const priceData = params[currentKey].split('-');
              result['filter_price_to'] = priceData[1];
              result['filter_price_from'] = priceData[0];
            }
          }
          if (currentKey === 'page' && params[currentKey] && parseInt(params[currentKey]) && !isNaN(parseInt(params[currentKey]))) {
            result['filter_offset'] = (parseInt(params[currentKey]) - 1) *  DEFAULT_PAGE_SIZE;
            result['filter_limit'] = parseInt(params[currentKey]) * DEFAULT_PAGE_SIZE;
            this.page = parseInt(params[currentKey]);
          }
          return result;
        }, { filter_offset: 0, filter_limit: DEFAULT_PAGE_SIZE });
        return this.vehicleService.searchCars({ ...queryParams });
      }),
      catchError(() => {
        this.cars = { total: 0, items: [] };
        this.cdr.markForCheck();
        return of([]);
      })
    ).subscribe(
      (data: Pagination<VehicleSchema>) => {
        this.cars = data;
        this.cdr.markForCheck();
      }
    );
  }

  ngOnDestroy() {
    this.onDestroy$.next(true);
    this.onDestroy$.complete();
  }

  onPageChange(page: number) {
    this.router.navigate(['searching'], { queryParams: { page }, queryParamsHandling: 'merge' })
  }

  constructor(
    private readonly cdr: ChangeDetectorRef,
    private readonly route: ActivatedRoute,
    private readonly router: Router,
    private readonly vehicleService: VehicleService,
  ) { }
}
