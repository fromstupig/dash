import { Component, OnInit, ChangeDetectionStrategy, Input, Output, EventEmitter, OnChanges, SimpleChanges, ChangeDetectorRef } from '@angular/core';
import { FilterEmmiterModel } from '@dash/types';
import { SearchFilterItem } from '@dealer-modules/car-searching/models/search-filter';
import { VehicleOptionModel } from '@dealer-modules/car-searching/models/vehicle/vehicle-option.model';

@Component({
  selector: 'dash-select-color',
  templateUrl: './select-color.component.html',
  styleUrls: ['./select-color.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SelectColorComponent implements OnInit, OnChanges {
  @Input() colors: VehicleOptionModel[];
  @Input() filter: SearchFilterItem;
  @Output('onColorChage') colorEmitter: EventEmitter<FilterEmmiterModel> = new EventEmitter<FilterEmmiterModel>();
  currentColor: string;

  ngOnInit(): void {
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes.filter) {
      this.currentColor = this.filter ? this.filter.value : '';;
      this.cdr.markForCheck();
    }
  }

  onSelectColor(color: VehicleOptionModel): void {
    const colorId: string = color.detail.code.toString();
    if (!this.currentColor || (colorId !== this.currentColor)) {
      this.currentColor = colorId;
      this.cdr.markForCheck();
    }
  }

  onFilter(): void {
    if (this.currentColor) {
      const color: VehicleOptionModel = this.colors.find((item: VehicleOptionModel) => item.detail.code.toString() === this.currentColor);
      console.log(color.detail.code.toString())
      if (color) this.colorEmitter.emit({ text: color.detail.title, value: color.detail.code.toString() });
    }
  }

  constructor(private cdr: ChangeDetectorRef) { }
}
