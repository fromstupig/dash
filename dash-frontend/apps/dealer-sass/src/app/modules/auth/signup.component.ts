import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { UserSignUpInfo } from './auth.model';


@Component({
  selector: 'dash-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignUpComponent implements OnInit {
  @Output() submitForm: EventEmitter<UserSignUpInfo> = new EventEmitter();
  @Output() redirectLogin: EventEmitter<any> = new EventEmitter();

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
      lastName: ['', Validators.required],
      firstName: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    });
  }

  onRedirectLogin() {
    this.redirectLogin.emit();
  }
}

