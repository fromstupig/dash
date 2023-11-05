import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BuildOwnCarComponent } from './build-own-car.component';

describe('BuildOwnCarComponent', () => {
  let component: BuildOwnCarComponent;
  let fixture: ComponentFixture<BuildOwnCarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BuildOwnCarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BuildOwnCarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
