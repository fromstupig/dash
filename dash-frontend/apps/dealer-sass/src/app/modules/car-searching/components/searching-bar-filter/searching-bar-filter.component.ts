import { Component, OnInit, Input, OnChanges, SimpleChanges, ChangeDetectionStrategy, ChangeDetectorRef, Output, EventEmitter, Inject, PLATFORM_ID } from '@angular/core';
import { SearchFilter, SearchFilterItem } from '@dealer-modules/car-searching/models/search-filter';
import { RemoveFilterData } from '@dealer-modules/car-searching/models/filter';
import { Clipboard } from '@angular/cdk/clipboard';
import { isPlatformBrowser } from '@angular/common';

@Component({
  selector: 'dash-searching-bar-filter',
  templateUrl: './searching-bar-filter.component.html',
  styleUrls: ['./searching-bar-filter.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SearchingBarFilterComponent implements OnInit, OnChanges {
  @Input('filters') listFilters: SearchFilter;
  @Output('removeFilter') removeFilterEmitter: EventEmitter<RemoveFilterData> = new EventEmitter<RemoveFilterData>();
  filters: Array<SearchFilterItem>;

  ngOnInit(): void {
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes.listFilters && changes.listFilters.currentValue) {
      this.filters = Object.keys(this.listFilters).map((key: string) => this.listFilters[key]).filter(item => item);
      this.cdr.markForCheck();
    }
  }

  removeFilter(filter: SearchFilterItem): void {
    this.removeFilterEmitter.emit({
      all: false,
      filter
    });
  }

  removeAllFilter(): void {
    this.removeFilterEmitter.emit({
      all: true,
      filter: null
    });
  }

  handleCopyLink(): void {
    if (isPlatformBrowser(this.platformId)) {
      this.clipboard.copy(window.location.href);
    }
  }

  constructor(
    private readonly cdr: ChangeDetectorRef,
    private readonly clipboard: Clipboard,
    @Inject(PLATFORM_ID) private readonly platformId: string
  ) { }
}
