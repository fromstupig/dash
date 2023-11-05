import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DashImageComponent } from './dash-image.component';

describe('DashImageComponent', () => {
  let component: DashImageComponent;
  let fixture: ComponentFixture<DashImageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DashImageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DashImageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
