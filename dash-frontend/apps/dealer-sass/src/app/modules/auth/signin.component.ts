import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { UserSignInInfo } from './auth.model';


@Component({
  selector: 'dash-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.scss']
})
export class SignInComponent implements OnInit {
  @Output() submitForm: EventEmitter<UserSignInInfo> = new EventEmitter();
  @Output() redirectSignup: EventEmitter<any> = new EventEmitter();

  formGroup: FormGroup;

  resetForm(): void {
    this.formGroup.reset();
  }

  constructor(private fb: FormBuilder) {
  }

  onSubmit() {
    this.submitForm.emit(this.formGroup.value);
  }

  ngOnInit(): void {
    this.formGroup = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    });
  }

  onRedirectSignup() {
    this.redirectSignup.emit();
  }
}

