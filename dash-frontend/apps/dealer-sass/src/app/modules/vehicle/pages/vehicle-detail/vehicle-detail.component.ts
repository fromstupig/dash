import { Component, OnInit, TemplateRef, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { NzModalRef, NzModalService } from 'ng-zorro-antd/modal';
import { Vehicle } from '../../../../../../../../libs/types/src';
import { DealType } from '../../components/payments/define';
import { AuthService } from '../../../auth/auth.service';
import { UserSignUpInfo, UserSignInInfo } from '../../../auth/auth.model';
import { PaymentService } from '../../payment.service';

@Component({
  selector: 'dash-vehicle-detail',
  templateUrl: './vehicle-detail.component.html',
  styleUrls: ['./vehicle-detail.component.scss']
})
export class VehicleDetailComponent implements OnInit {
  @ViewChild('signup') public signupRef: TemplateRef<any>;
  @ViewChild('signin') public signinRef: TemplateRef<any>;

  signUpModal: NzModalRef;
  signInModal: NzModalRef;
  isSubmitting: boolean;
  vehicle: Vehicle;
  isTabSelect: boolean = false;
  exteriors: string[] = [];
  interiors: string[] = [];
  dealType = DealType;
  paymentOptions = {
    current: DealType.Cash,
    [DealType.Lease]: {},
    [DealType.Finance]: {},
    [DealType.Cash]: {}
  };
  currentUser: any = null;
  msrp = 0;
  term = 0;

  isAllFeatureModal: boolean = false;

  constructor(private route: ActivatedRoute,
              private modal: NzModalService,
              private authService: AuthService,
              private paymentService: PaymentService) {
  }

  ngOnInit(): void {
    this.vehicle = this.route.snapshot.data['vehicle'].data;
    this.vehicle.galleries.forEach((g) => {
      if (g.type === 'EXTERIOR') this.exteriors.push(g.asset_path);
      else if (g.type === 'INTERIOR') this.interiors.push(g.asset_path);
    });
    this.authService.getCredentialFromStore().subscribe(
      (userInfo) => {
        if (userInfo) {
          this.currentUser = userInfo;
        }
      }
    );
  }

  showAllFeatureModal() {
    this.isAllFeatureModal = true;
  }

  handleCancelModal(): void {
    this.isAllFeatureModal = false;
  }

  handleTabChange(): void {
    if (!this.isTabSelect) this.isTabSelect = true;
  }

  onNextStep() {
    this.isSubmitting = true;
    if (!this.currentUser) {
      this.signUpModal = this.modal.create({
        nzContent: this.signupRef,
        nzFooter: null
      });
    } else {
      this.purchase();
    }
  }

  onSignUp(userSignUpInfo: UserSignUpInfo) {
    this.authService.register(userSignUpInfo).subscribe(
      (userInfo) => {
        this.currentUser = this.authService.saveCredentialToStore(userInfo);
        this.signUpModal.close();
        this.purchase();
      }
    );
  }

  onSelectPaymentMethod(type: string) {
    this.paymentOptions.current = type;
    this.onPaymentUpdate();
  }

  onPaymentUpdate() {
    const type = this.paymentOptions.current;
    this.msrp = +(this.paymentOptions[type] as any).pricing.msrp;

    if (type === this.dealType.Lease) {
      this.term = +(this.paymentOptions[type] as any).lease.monthlyPayment.total;
    } else if (type === this.dealType.Finance) {
      this.term = +(this.paymentOptions[type] as any).loan.downPayment;
    } else {
      this.term = 0;
    }
  }

  onSignIn(userSignInInfo: UserSignInInfo) {
    this.authService.login(userSignInInfo).subscribe(
      (userInfo) => {
        this.currentUser = this.authService.saveCredentialToStore(userInfo);
        this.signInModal.close();
        this.purchase();
      }
    );
  }

  showLoginDialog() {
    this.signUpModal.close();
    if (!this.currentUser) {
      this.signInModal = this.modal.create({
        nzContent: this.signinRef,
        nzFooter: null
      });
    }
  }

  showSignupDialog() {
    this.signInModal.close();
    if (!this.currentUser) {
      this.signUpModal = this.modal.create({
        nzContent: this.signupRef,
        nzFooter: null
      });
    }
  }

  purchase() {
    const params = {
      'requester_email': this.currentUser.user.email,
      'requester_phone_number': this.currentUser.user.phone_number || '',
      'vehicle_id': this.vehicle.id,
      'user_id': this.currentUser.user.id,
      'pricing_detail': this.paymentOptions[this.paymentOptions.current]
    };

    this.paymentService.makeDealerRequest(params).subscribe(data => {
      this.isSubmitting = false;
      console.log(data);
    });
  }
}
