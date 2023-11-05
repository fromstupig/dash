import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ApplicationRoutingModule } from './application-routing.module';
import { ApplicationComponent } from './application.component';
import { NzTableModule } from 'ng-zorro-antd/table';
import { RequestService } from './request.service';


@NgModule({
  declarations: [ApplicationComponent],
  imports: [
    CommonModule,
    ApplicationRoutingModule,
    NzTableModule
  ],
  providers: [RequestService]
})
export class ApplicationModule { }
