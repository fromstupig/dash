import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SugesstionComponent } from './sugesstion.component';

describe('SugesstionComponent', () => {
  let component: SugesstionComponent;
  let fixture: ComponentFixture<SugesstionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SugesstionComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SugesstionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
