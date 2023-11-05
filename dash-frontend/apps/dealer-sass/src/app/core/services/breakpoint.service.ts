import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BreakpointService {
  private isMobileDeviceSource: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);
  public isMobileDevice: Observable<boolean> = this.isMobileDeviceSource.asObservable();

  public setIsMobileDevice(nextState: boolean): void {
    if (this.isMobileDeviceSource.value !== nextState) {
      this.isMobileDeviceSource.next(nextState);
    }
  }
}
