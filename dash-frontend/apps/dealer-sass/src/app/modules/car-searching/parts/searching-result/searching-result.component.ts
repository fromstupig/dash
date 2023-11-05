import { ChangeDetectionStrategy, Component, Input, OnDestroy, OnInit } from '@angular/core';
import { VehicleSchema } from '@dealer-modules/car-searching/models/vehicle/vehicle.model';
import { Router } from '@angular/router';
import { NzModalService } from 'ng-zorro-antd/modal';
import { BuildOwnCarComponent } from '../../../../components/modals/build-own-car/build-own-car.component';

@Component({
  selector: 'dash-searching-result',
  templateUrl: './searching-result.component.html',
  styleUrls: ['./searching-result.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SearchingResultComponent implements OnInit, OnDestroy {
  @Input() cars: VehicleSchema[];
  
  ngOnInit(): void {
  }

  ngOnDestroy(): void {
  }
  
  constructor(private router: Router, private modalService: NzModalService) { }

  public resetFilter() {
    this.router.navigateByUrl('/searching');
  }

  public openModalBuild() {
    this.modalService.create({
      nzTitle: null,
      nzFooter: null,
      nzWidth: '800px',
      nzStyle: { 'border-radius': '20px' },
      nzContent: BuildOwnCarComponent
    })
  }
}
