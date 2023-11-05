import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchingBarFilterComponent } from './searching-bar-filter.component';

describe('SearchingBarFilterComponent', () => {
  let component: SearchingBarFilterComponent;
  let fixture: ComponentFixture<SearchingBarFilterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SearchingBarFilterComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchingBarFilterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
