import { Component, OnInit, ChangeDetectionStrategy, Input } from '@angular/core';
import { VehicleSchema } from '@dealer-modules/car-searching/models/vehicle/vehicle.model';

@Component({
  selector: 'dash-searching-item',
  templateUrl: './searching-item.component.html',
  styleUrls: ['./searching-item.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SearchingItemComponent implements OnInit {
  @Input() car: VehicleSchema;
  constructor() { }

  ngOnInit(): void {
  }

}
