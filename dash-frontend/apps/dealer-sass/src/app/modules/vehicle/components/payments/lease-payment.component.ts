import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Vehicle } from '../../../../../../../../libs/types/src';
import { PaymentService } from '../../payment.service';
import { DealType, DefaultVehicle, LeasePayment } from './define';
import { FormBuilder, FormGroup } from '@angular/forms';
import { debounceTime } from 'rxjs/operators';

@Component({
  selector: 'dash-vehicle-lease-payment',
  templateUrl: './lease-payment.component.html',
  styleUrls: ['./lease-payment.component.scss']
})
export class VehicleLeasePaymentComponent implements OnInit {
  @Input() vehicle: Vehicle;
  @Input() dealInformation!: any;
  @Input() editMode = false;
  @Output() dealInformationChange: EventEmitter<any> = new EventEmitter<any>();
  loading = false;
  amountMax = 50000;
  amount = 0;

  leasePayment = LeasePayment;
  formGroup: FormGroup;

  constructor(private paymentService: PaymentService, private fb: FormBuilder) {
  }

  ngOnInit(): void {
    this.amount = this.leasePayment.default.dueAtSigningAmount;

    this.formGroup = this.fb.group({
      mileage: this.leasePayment.default.mileage,
      term: this.leasePayment.default.term,
      amount: this.leasePayment.default.dueAtSigningAmount
    });

    this.getPayment(DefaultVehicle.vin, DealType.Lease,
      this.leasePayment.default.dueAtSigningAmount, this.leasePayment.default.mileage,
      this.leasePayment.default.term);

    this.formGroup.valueChanges.pipe(debounceTime(500)).subscribe(
      ({ mileage, term, amount }: any) => {
        this.getPayment(DefaultVehicle.vin, DealType.Lease, amount, mileage, term);
      });
  }

  onAmountChange(amount: number) {
    this.amount = amount;
    this.formGroup.controls['amount'].setValue(this.amount);
  }

  getPayment(vin: string, dealType: string, dueAtSigningAmount: number,
             mileage: number, term: number) {
    this.loading = true;
    this.paymentService.getPaymentByDeal({
      'dealType': dealType,
      'vin': vin,
      'dueAtSigningAmount': dueAtSigningAmount,
      'mileage': mileage,
      'term': term
    }).subscribe(data => {
      this.onDealChange(data.dealInformation);
      this.amountMax = +this.dealInformation.pricing.msrp;
      this.loading = false;
    });
  }


  onDealChange(data) {
    this.dealInformation = data;
    this.dealInformationChange.emit(this.dealInformation);
  }
}
