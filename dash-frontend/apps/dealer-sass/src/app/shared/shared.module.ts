import { NgModule, ModuleWithProviders } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { IconsProviderModule } from './icons-provider.module';
import { NzLayoutModule } from 'ng-zorro-antd/layout';
import { NzGridModule } from 'ng-zorro-antd/grid';
import { NzButtonModule } from 'ng-zorro-antd/button';
import { NzInputModule } from 'ng-zorro-antd/input';
import { NzInputNumberModule } from 'ng-zorro-antd/input-number';

@NgModule({
  declarations: [],
  imports: [CommonModule],
  exports: [
    CommonModule,
    HttpClientModule,
    FormsModule,
    IconsProviderModule,
    NzLayoutModule,
    NzGridModule,
    NzButtonModule,
    NzInputModule,
    NzInputNumberModule
  ]
})
export class SharedModule {
}
