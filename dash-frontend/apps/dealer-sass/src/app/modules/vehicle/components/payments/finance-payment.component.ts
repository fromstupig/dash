import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Vehicle } from '../../../../../../../../libs/types/src';
import { DealType, DefaultVehicle, LeasePayment, LoanPayment } from './define';
import { FormBuilder, FormGroup } from '@angular/forms';
import { PaymentService } from '../../payment.service';
import { debounceTime } from 'rxjs/operators';

@Component({
  selector: 'dash-finance-payment',
  templateUrl: './finance-payment.component.html',
  styleUrls: ['./finance-payment.component.scss', './lease-payment.component.scss']
})
export class VehicleFinancePaymentComponent implements OnInit {
  @Input() vehicle: Vehicle;
  @Input() dealInformation!: any;
  @Input() editMode = false;
  @Output() dealInformationChange: EventEmitter<any> = new EventEmitter<any>();
  loading = false;
  amountMax = 50000;
  amount = 0;

  loanPayment = LoanPayment;
  formGroup: FormGroup;
  apr: number;

  constructor(private paymentService: PaymentService, private fb: FormBuilder) {
  }

  ngOnInit(): void {
    this.amount = this.loanPayment.default.downPayment;

    this.formGroup = this.fb.group({
      term: this.loanPayment.default.term,
      amount: this.loanPayment.default.downPayment
    });

    this.getPayment(DefaultVehicle.vin, DealType.Finance,
      this.loanPayment.default.downPayment, this.loanPayment.default.term);

    this.formGroup.valueChanges.pipe(debounceTime(500)).subscribe(
      ({ term, amount }: any) => {
        this.getPayment(DefaultVehicle.vin, DealType.Finance, amount, term);
      });
  }

  onAmountChange(amount: number) {
    this.amount = amount;
    this.formGroup.controls['amount'].setValue(this.amount);
  }

  getPayment(vin: string, dealType: string, downPayment: number,
             term: number) {
    this.loading = true;
    this.paymentService.getPaymentByDeal({
      'dealType': dealType,
      'vin': vin,
      'downPayment': downPayment,
      'term': term
    }).subscribe(data => {
      this.onDealChange(data.dealInformation);
      this.apr = +this.dealInformation.loan.apr.value;
      this.amountMax = +this.dealInformation.pricing.msrp;
      this.loading = false;
    });
  }

  onDealChange(data) {
    this.dealInformation = data;
    this.dealInformationChange.emit(this.dealInformation);
  }
}
