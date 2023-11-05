import {
  ChangeDetectionStrategy,
  Component,
  Input,
  OnInit
} from '@angular/core'

@Component({
  selector: 'dash-vehicle-deatail-header',
  templateUrl: './vehicle-deatail-header.component.html',
  styleUrls: ['./vehicle-deatail-header.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class VehicleDeatailHeaderComponent implements OnInit {
  @Input() modelName: string
  @Input() modelCode: string

  constructor() {}

  ngOnInit(): void {}
}
