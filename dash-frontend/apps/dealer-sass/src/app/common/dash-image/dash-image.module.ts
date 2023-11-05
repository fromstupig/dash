import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DashImageComponent } from './dash-image.component';

@NgModule({
  declarations: [DashImageComponent],
  imports: [
    CommonModule
  ],
  exports: [DashImageComponent]
})
export class DashImageModule { }
