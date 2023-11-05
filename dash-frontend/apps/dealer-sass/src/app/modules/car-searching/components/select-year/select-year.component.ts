import { Component, OnInit, ChangeDetectionStrategy, Input, Output, EventEmitter, OnChanges, ChangeDetectorRef, SimpleChanges } from '@angular/core';
import { SearchFilterItem } from '@dealer-modules/car-searching/models/search-filter';
import { FilterEmmiterModel } from '@dash/types';
import { VehicleYearModel } from '@dealer-modules/car-searching/models/vehicle/vehicle-year.model';

@Component({
  selector: 'dash-select-year',
  templateUrl: './select-year.component.html',
  styleUrls: ['./select-year.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SelectYearComponent implements OnInit, OnChanges {
  @Input() years: VehicleYearModel[];
  @Input() filter: SearchFilterItem;
  @Input() showFooter: boolean = true;
  @Output('onYearChange') yearChangeEmitter: EventEmitter<FilterEmmiterModel> = new EventEmitter<FilterEmmiterModel>();
  currentYear: string;

  ngOnInit(): void {
  }

  onSelectYear(year: any): void {
    if (!this.currentYear || (year.id.toString() !== this.currentYear)) {
      this.currentYear = year.id.toString();
      this.cdr.markForCheck();
    }
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes.filter) {
      this.currentYear = this.filter ? this.filter.value : '';;
      this.cdr.markForCheck();
    }
  }

  onFilter(): void {
    if (this.currentYear) {
      const year = this.years.find((yearModel: VehicleYearModel) => yearModel.id.toString() === this.currentYear.toString())
      this.yearChangeEmitter.emit({
        text: year.year.toString(),
        value: year.id.toString()
      });
    }
  }

  constructor(private cdr: ChangeDetectorRef) { }
}
