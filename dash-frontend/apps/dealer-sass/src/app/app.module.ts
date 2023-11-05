import { BrowserModule } from '@angular/platform-browser'
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'
import { NgModule } from '@angular/core'
import { HttpClientModule } from '@angular/common/http'

import { APP_CONFIG } from '@dash/config';
import { environment } from '../environments/environment'

import { CoreModule } from './core/core.module';

import { AppComponent } from './app.component'
import { AppRoutingModule } from './app-routing.module'

import { en_US, NZ_I18N } from 'ng-zorro-antd/i18n'
import { AngularSvgIconModule } from 'angular-svg-icon'
import { IconsProviderModule } from '@dealer-shared/icons-provider.module'
import { NzLayoutModule } from 'ng-zorro-antd/layout'
import { NzGridModule } from 'ng-zorro-antd/grid'
import { NzMenuModule } from 'ng-zorro-antd/menu'
import { NzButtonModule } from 'ng-zorro-antd/button'
import { NzInputModule } from 'ng-zorro-antd/input'
import { MainFooterComponent } from './components/main-footer/main-footer.component'

@NgModule({
  declarations: [AppComponent, MainFooterComponent],
  imports: [
    BrowserModule.withServerTransition({ appId: 'serverApp' }),
    BrowserAnimationsModule,
    AppRoutingModule,
    HttpClientModule,
    AngularSvgIconModule.forRoot(),
    IconsProviderModule,
    NzLayoutModule,
    NzGridModule,
    NzMenuModule,
    NzButtonModule,
    NzInputModule,
    CoreModule,
    NzInputModule
  ],
  providers: [
    { provide: NZ_I18N, useValue: en_US },
    { provide: APP_CONFIG, useValue: environment }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
