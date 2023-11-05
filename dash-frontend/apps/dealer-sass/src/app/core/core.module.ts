import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
/* Modules Dependency */
import { NzIconModule } from 'ng-zorro-antd/icon';
import { AngularSvgIconModule } from 'angular-svg-icon';
import { NzDrawerModule } from 'ng-zorro-antd/drawer';
/* Components */
import { LayoutFooterComponent } from '@dealer-core/layouts/layout-footer/layout-footer.component';
import { LayoutHeaderComponent } from '@dealer-core/layouts/layout-header/layout-header.component';
import { FooterQuickAccessComponent } from '@dealer-core/components/footer-quick-access/footer-quick-access.component';
import { HomeService } from '@dealer-modules/home/services/home.service';
import { AuthModule } from '@dealer-modules/auth/auth.module';
import { NzModalModule } from 'ng-zorro-antd/modal';

@NgModule({
  declarations: [
    LayoutFooterComponent,
    LayoutHeaderComponent,
    FooterQuickAccessComponent,
  ],
  imports: [
    CommonModule,
    AngularSvgIconModule,
    NzIconModule,
    NzDrawerModule,
    RouterModule,
    AuthModule,
    NzModalModule
  ],
  providers: [
    HomeService
  ],
  exports: [LayoutHeaderComponent, LayoutFooterComponent]
})
export class CoreModule { }
