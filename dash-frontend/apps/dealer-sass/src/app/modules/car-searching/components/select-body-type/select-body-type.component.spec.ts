import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SelectBodyTypeComponent } from './select-body-type.component';

describe('SelectBodyTypeComponent', () => {
  let component: SelectBodyTypeComponent;
  let fixture: ComponentFixture<SelectBodyTypeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SelectBodyTypeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SelectBodyTypeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
