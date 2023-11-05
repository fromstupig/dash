import {
  Component,
  OnInit,
  ChangeDetectionStrategy,
  Input,
  OnChanges,
  SimpleChanges,
  ChangeDetectorRef,
  Output,
  EventEmitter
} from '@angular/core'
import { FilterEmmiterModel } from '@dash/types'
import { SearchFilterItem } from '@dealer-modules/car-searching/models/search-filter'

@Component({
  selector: 'dash-select-price-range',
  templateUrl: './select-price-range.component.html',
  styleUrls: ['./select-price-range.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SelectPriceRangeComponent implements OnInit, OnChanges {
  @Input() defaultPrice: SearchFilterItem = {
    value: '2000-18000',
    text: '2000-18000',
    type: 'price'
  }
  @Input() showFooter: boolean = true
  @Output('onPriceChange') priceChangeEmiter: EventEmitter<
    FilterEmmiterModel
  > = new EventEmitter<FilterEmmiterModel>();
  price: [number, number] = [2000, 18000]

  ngOnInit(): void {}

  ngOnChanges(changes: SimpleChanges) {
    if (
      changes &&
      changes.defaultPrice &&
      changes.defaultPrice.currentValue &&
      changes.defaultPrice.currentValue.value
    ) {
      if (this.defaultPrice.value === '>20000') {
        this.price = [0, 20000];
      } else {
        this.price = this.defaultPrice.value.split('-').map(parseFloat) as [
          number,
          number
        ]
      }
      this.cdr.markForCheck()
    }
  }

  onFilter() {
    this.emitFilterPriceChange();
  }

  afterChange() {
    if (!this.showFooter) {
      this.emitFilterPriceChange();
    }
  }

  private emitFilterPriceChange(): void {
    let result: string = this.price.join('-');
    if (this.price[1] === 20000) {
      result = '>20000';
    }
    this.priceChangeEmiter.emit({
      value: result,
      text: result
    });
  }

  constructor(private readonly cdr: ChangeDetectorRef) {}
}
