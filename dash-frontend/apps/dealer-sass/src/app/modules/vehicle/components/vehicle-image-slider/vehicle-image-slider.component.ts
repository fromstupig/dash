import {
  Component,
  Input,
  ViewChild,
  AfterViewInit,
  OnInit
} from '@angular/core'

@Component({
  selector: 'dash-vehicle-image-slider',
  templateUrl: './vehicle-image-slider.component.html',
  styleUrls: ['./vehicle-image-slider.component.scss']
})
export class VehicleImageSliderComponent implements OnInit, AfterViewInit {
  @ViewChild('viewer') viewer: any
  @Input() imageUrls: string[]
  imageUrlsString: string

  constructor() {}

  ngOnInit() {}

  ngAfterViewInit() {
    const urls = this.imageUrls.map((image) => `"${image}"`)
    setTimeout(() => {
      const reverse = urls.reverse();
      this.imageUrlsString = `[${reverse.join(',')}]`;
      setTimeout(() => (window as any).CI360.init(), 0);
    }, 0)
  }
}
