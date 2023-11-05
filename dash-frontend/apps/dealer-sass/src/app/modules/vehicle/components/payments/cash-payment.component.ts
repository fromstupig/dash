import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Vehicle } from '../../../../../../../../libs/types/src';
import { DealType, DefaultVehicle, LoanPayment } from './define';
import { FormGroup } from '@angular/forms';
import { PaymentService } from '../../payment.service';

@Component({
  selector: 'dash-cash-payment',
  templateUrl: './cash-payment.component.html',
  styleUrls: ['./cash-payment.component.scss', 'lease-payment.component.scss']
})
export class VehicleCashPaymentComponent implements OnInit {
  @Input() vehicle: Vehicle;
  @Input() dealInformation!: any;
  @Input() editMode = false;
  @Output() dealInformationChange: EventEmitter<any> = new EventEmitter<any>();
  loading = false;

  constructor(private paymentService: PaymentService) {
  }

  ngOnInit(): void {
    this.getPayment(DefaultVehicle.vin, DealType.Cash);
  }

  getPayment(vin: string, dealType: string) {
    this.loading = true;
    this.paymentService.getPaymentByDeal({
      'dealType': dealType,
      'vin': vin,
    }).subscribe(data => {
      this.onDealChange(data.dealInformation);
      this.loading = false;
    });
  }

  onDealChange(data) {
    this.dealInformation = data;
    this.dealInformationChange.emit(this.dealInformation);
  }
}
