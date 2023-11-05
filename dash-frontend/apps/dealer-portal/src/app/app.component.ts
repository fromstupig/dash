import { Component } from '@angular/core';

interface MenuItem {
  title: string;
  icon: string;
  link: string;
  level: number;
  children?: MenuItem[];
}

@Component({
  selector: 'dash-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  isCollapsed = false;
  menus: MenuItem[] = [{
    title: 'Dashboard',
    icon: 'rise',
    link: '/dashboard',
    level: 1
  }, {
    title: 'Applications',
    icon: 'carry-out',
    link: '/applications',
    level: 1
  }];
}
