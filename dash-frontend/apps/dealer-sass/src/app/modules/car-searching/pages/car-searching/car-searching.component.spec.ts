import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarSearchingComponent } from './car-searching.component';

describe('CarSearchingComponent', () => {
  let component: CarSearchingComponent;
  let fixture: ComponentFixture<CarSearchingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CarSearchingComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CarSearchingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
