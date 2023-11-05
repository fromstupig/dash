import {
  ChangeDetectionStrategy,
  Component,
  Input,
  OnInit
} from '@angular/core'

@Component({
  selector: 'dash-vehicle-feature-col',
  templateUrl: './vehicle-feature-col.component.html',
  styleUrls: ['./vehicle-feature-col.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class VehicleFeatureColComponent implements OnInit {
  @Input() name: string
  @Input() iconPath: string

  constructor() {}

  ngOnInit(): void {}
}
