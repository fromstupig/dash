import { Component, OnInit, ChangeDetectionStrategy, Input, EventEmitter, Output, OnChanges } from '@angular/core';
import { DEFAULT_PAGE_SIZE } from '@dealer-modules/car-searching/constants/pagination.constant';

@Component({
  selector: 'dash-pagination',
  templateUrl: './pagination.component.html',
  styleUrls: ['./pagination.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class PaginationComponent implements OnInit, OnChanges {
  @Input() total: number;
  @Input() page: number;
  @Output() onPageChange: EventEmitter<number> = new EventEmitter<number>();
  pageSize: number = DEFAULT_PAGE_SIZE;

  currentStartItem: number = 1;
  currentEndItem: number = 1;

  constructor() { }

  ngOnInit(): void {
  }

  ngOnChanges(): void {
    const start = (this.page - 1) * this.pageSize;
    this.currentStartItem = start > 0 ? start : 1;
    this.currentEndItem = (start + this.pageSize) > this.total ? this.total : (start + this.pageSize);
  }

  onPageChangeIndex(page: number) {
    this.onPageChange.emit(page);
  }
}
