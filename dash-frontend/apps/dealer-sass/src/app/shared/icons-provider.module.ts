import { NgModule } from '@angular/core'
import { NZ_ICONS, NzIconModule } from 'ng-zorro-antd/icon'

import {
  MenuFoldOutline,
  MenuUnfoldOutline,
  FormOutline,
  DashboardOutline,
  SearchOutline,
  ShareAltOutline,
  MenuOutline,
  AimOutline,
  PhoneFill,
} from '@ant-design/icons-angular/icons';

const icons = [
  MenuFoldOutline,
  MenuUnfoldOutline,
  DashboardOutline,
  FormOutline,
  SearchOutline,
  ShareAltOutline,
  MenuOutline,
  AimOutline,
  PhoneFill,
];

@NgModule({
  imports: [NzIconModule],
  exports: [NzIconModule],
  providers: [{ provide: NZ_ICONS, useValue: icons }]
})
export class IconsProviderModule {}
