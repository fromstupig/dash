import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchingBannerComponent } from './searching-banner.component';

describe('SearchingBannerComponent', () => {
  let component: SearchingBannerComponent;
  let fixture: ComponentFixture<SearchingBannerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SearchingBannerComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchingBannerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
