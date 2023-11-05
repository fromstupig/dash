import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SelectPriceRangeComponent } from './select-price-range.component';

describe('SelectPriceRangeComponent', () => {
  let component: SelectPriceRangeComponent;
  let fixture: ComponentFixture<SelectPriceRangeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SelectPriceRangeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SelectPriceRangeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
