import { NgModule } from '@angular/core';
import { SignUpComponent } from './signup.component';
import { NzFormModule } from 'ng-zorro-antd/form';
import { NzInputModule } from 'ng-zorro-antd/input';
import { ReactiveFormsModule } from '@angular/forms';
import { SharedModule } from '../../shared/shared.module';
import { AuthService } from './auth.service';
import { SignInComponent } from './signin.component';

@NgModule({
  declarations: [
    SignUpComponent,
    SignInComponent
  ],
  imports: [
    NzFormModule,
    NzInputModule,
    ReactiveFormsModule,
    SharedModule
  ],
  exports: [
    SignUpComponent,
    SignInComponent
  ],
  providers: [
    AuthService
  ]

})
export class AuthModule{}
