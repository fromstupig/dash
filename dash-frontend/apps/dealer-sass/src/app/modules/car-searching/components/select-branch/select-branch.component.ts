import { Component, OnInit, ChangeDetectionStrategy, Input, ViewEncapsulation, OnChanges, SimpleChanges, ChangeDetectorRef, Output, EventEmitter } from '@angular/core';
import { VehicleBranchModelData } from '@dealer-modules/car-searching/models/vehicle/vehicle-branch.model';
import { FilterEmmiterModel } from '@dash/types'; 
import { SearchFilterItem } from '../../models/search-filter';

@Component({
  selector: 'dash-select-branch',
  templateUrl: './select-branch.component.html',
  styleUrls: ['./select-branch.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  encapsulation: ViewEncapsulation.None
})
export class SelectBranchComponent implements OnInit, OnChanges {
  @Input() branches: VehicleBranchModelData[] = [];
  @Input() filter: SearchFilterItem;
  @Input() showFooter: boolean = true;
  @Output('onBranchChage') branchEmitter: EventEmitter<FilterEmmiterModel> = new EventEmitter<FilterEmmiterModel>();
  currentBranch: string;

  ngOnInit(): void {
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes.filter) {
      this.currentBranch = this.filter ? this.filter.value.toString() : '';
      this.cdr.markForCheck();
    }
  }

  onSelectBranch(branch: VehicleBranchModelData): void {
    if (!this.currentBranch || (branch.id.toString() !== this.currentBranch)) {
      this.currentBranch = branch.id.toString();
      this.cdr.markForCheck();
    }
  }

  onFilter(): void {
    if (this.currentBranch) {
      const branch: VehicleBranchModelData = this.branches.find((item: VehicleBranchModelData) => item.id.toString() === this.currentBranch.toString());
      if (branch) {
        this.branchEmitter.emit({ text: branch.name, value: this.currentBranch });
      }
    }
  }

  constructor(private cdr: ChangeDetectorRef) { }
}
