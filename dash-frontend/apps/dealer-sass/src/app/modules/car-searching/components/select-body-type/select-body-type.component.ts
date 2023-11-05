import { Component, OnInit, ChangeDetectionStrategy, Input, EventEmitter, Output, OnChanges, SimpleChanges, ChangeDetectorRef } from '@angular/core';
import { FilterEmmiterModel } from '@dash/types';
import { SearchFilterItem } from '@dealer-modules/car-searching/models/search-filter';
import { VehicleBodyModel } from '@dealer-modules/car-searching/models/vehicle/vehicle-body.nodel';

@Component({
  selector: 'dash-select-body-type',
  templateUrl: './select-body-type.component.html',
  styleUrls: ['./select-body-type.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SelectBodyTypeComponent implements OnInit, OnChanges {
  @Input() bodies: VehicleBodyModel[];
  @Input() filter: SearchFilterItem;
  @Input() showFooter: boolean = true;
  currentBodyType: string;
  @Output('onBodyTypeChange') bodyTypeEmitter: EventEmitter<FilterEmmiterModel> = new EventEmitter<FilterEmmiterModel>();

  ngOnInit(): void {
  }

  onSelectBodyType(bodyType: VehicleBodyModel): void {
    const bodyTypeId: string = bodyType.id.toString()
    if (!this.currentBodyType || (bodyTypeId !== this.currentBodyType)) {
      this.currentBodyType = bodyTypeId;
      this.cdr.markForCheck();
    }
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes.filter) {
      this.currentBodyType = this.filter ? this.filter.value : '';
      this.cdr.markForCheck();
    }
  }

  onFilter(): void {
    if (this.currentBodyType) {
      const bodyType: VehicleBodyModel = this.bodies.find((bodyTypeItem: VehicleBodyModel) => bodyTypeItem.id.toString() === this.currentBodyType);
      if (bodyType) this.bodyTypeEmitter.emit({ text: bodyType.name, value: bodyType.id.toString() });
    }
  }

  constructor(private cdr: ChangeDetectorRef) { }
}
