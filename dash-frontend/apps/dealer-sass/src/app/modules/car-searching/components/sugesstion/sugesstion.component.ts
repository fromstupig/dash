import { Component, OnInit } from '@angular/core';
import { BuildOwnCarComponent } from '../../../../components/modals/build-own-car/build-own-car.component';
import { NzModalService } from 'ng-zorro-antd/modal';

@Component({
  selector: 'dash-sugesstion',
  templateUrl: './sugesstion.component.html',
  styleUrls: ['./sugesstion.component.scss']
})
export class SugesstionComponent implements OnInit {
  isShowModal: boolean = false;

  constructor(private modalService: NzModalService) { }

  ngOnInit(): void {
  }

  showModalBuildCar(): void {
    this.modalService.create({
      nzTitle: null,
      nzFooter: null,
      nzWidth: '800px',
      nzStyle: { 'border-radius': '20px' },
      nzContent: BuildOwnCarComponent
    })
  }
}
