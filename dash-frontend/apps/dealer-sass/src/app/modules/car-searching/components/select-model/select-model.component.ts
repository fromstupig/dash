import { Component, OnInit, ChangeDetectionStrategy, Input, OnChanges, Output, EventEmitter, SimpleChanges, ChangeDetectorRef } from '@angular/core';
import { SearchFilterItem } from '@dealer-modules/car-searching/models/search-filter';
import { VehicleModelModel } from '@dealer-modules/car-searching/models/vehicle/vehicle-model.model';
import { FilterEmmiterModel } from '@dash/types';

@Component({
  selector: 'dash-select-model',
  templateUrl: './select-model.component.html',
  styleUrls: ['./select-model.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SelectModelComponent implements OnInit, OnChanges {
  @Input() models: Array<VehicleModelModel>;
  @Input() filter: SearchFilterItem;
  @Input() showFooter: boolean = true;
  @Output('onModelChange') modelChangeEmiter: EventEmitter<FilterEmmiterModel> = new EventEmitter<FilterEmmiterModel>();
  currentModal: string;

  ngOnInit(): void {
  }

  onSelectModel(model: any): void {
    if (!this.currentModal || (model.id.toString() !== this.currentModal)) {
      this.currentModal = model.id.toString();
      this.cdr.markForCheck();
    }
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes.filter) {
      this.currentModal = this.filter ? this.filter.value : '';;
      this.cdr.markForCheck();
    }
  }

  onFilter(): void {
    if (this.currentModal) {
      const model: VehicleModelModel = this.models.find((modelItem: VehicleModelModel) => modelItem.id.toString()  === this.currentModal);
      this.modelChangeEmiter.emit({ text: model.name, value: model.id.toString() });
    }
  }

  constructor(private cdr: ChangeDetectorRef) { }
}
