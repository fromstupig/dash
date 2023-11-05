import { Component, OnInit, ChangeDetectionStrategy, Input } from '@angular/core';

@Component({
  selector: 'dash-image',
  templateUrl: './dash-image.component.html',
  styleUrls: ['./dash-image.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class DashImageComponent implements OnInit {
  @Input() src: string;
  @Input() alt: string;
  
  constructor() { }

  ngOnInit(): void {
  }

}
