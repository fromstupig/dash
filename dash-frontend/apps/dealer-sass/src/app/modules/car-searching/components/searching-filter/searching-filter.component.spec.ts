import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchingFilterComponent } from './searching-filter.component';

describe('SearchingFilterComponent', () => {
  let component: SearchingFilterComponent;
  let fixture: ComponentFixture<SearchingFilterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SearchingFilterComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchingFilterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
