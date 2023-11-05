import { Component, Inject, OnDestroy, OnInit, PLATFORM_ID } from '@angular/core';
import { fromEvent, Subject } from 'rxjs';
import { isPlatformBrowser } from '@angular/common';
import { distinctUntilChanged, filter, map, takeUntil, tap } from 'rxjs/operators';
import { BreakpointService } from '@dealer-core/services/breakpoint.service';

@Component({
  selector: 'dash-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit, OnDestroy {
  public isOnTop = true;
  private onDestroy$: Subject<boolean> = new Subject<boolean>();

  ngOnInit(): void {
    // If platform is browser, will register resize and scroll event.
    // Must check platform browser because when build universal, window or document is not defined
    if (isPlatformBrowser(this.platformId)) {
      this.onResizeWindowAction();
      this.onScrollWindowAction();
    }
    // Detect mobile when load page
    this.detectIsMobile();
  }

  ngOnDestroy() {
    // Notify destroy was dispatch and complete subject
    this.onDestroy$.next(true);
    this.onDestroy$.complete();
  }

  /**
   * Register listen scroll event.
   * Get pageYOffset in window and detect is on top or not
   * If pageYOffset < 20, it is on top
   * @returns {void}
   */
  private onScrollWindowAction(): void {
    fromEvent(window, 'scroll').pipe(
      takeUntil(this.onDestroy$),
      distinctUntilChanged(),
      map(() => window.pageYOffset),
      filter((pageYOffset: number) => this.isOnTop !== (pageYOffset < 20))
    ).subscribe((pageYOffset: number) => {
      this.isOnTop = pageYOffset < 20;
    });
  }

  /**
   * Register listen resize event on window
   * Detect is mobile or not in detectIsMobile method.
   * @returns {void}
   */
  private onResizeWindowAction(): void {
    fromEvent(window, 'resize').pipe(
      takeUntil(this.onDestroy$),
      distinctUntilChanged()
    ).subscribe(() => this.detectIsMobile());
  }

  /**
   * Detect is mobile or not. Dependency on window width
   * If window scroll and device change. update in BreakpointService.
   * @returns {void}
   */
  private detectIsMobile(): void {
    this.breakpointService.setIsMobileDevice(window.innerWidth < 992);
  }

  constructor(
    @Inject(PLATFORM_ID) private readonly platformId: string,
    private readonly breakpointService: BreakpointService
  ) {}
}
