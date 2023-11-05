import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'dash-footer-quick-access',
  templateUrl: './footer-quick-access.component.html',
  styleUrls: ['./footer-quick-access.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class FooterQuickAccessComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
