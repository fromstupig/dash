import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchingItemComponent } from './searching-item.component';

describe('SearchingItemComponent', () => {
  let component: SearchingItemComponent;
  let fixture: ComponentFixture<SearchingItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SearchingItemComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchingItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
