import {
  Component,
  OnInit,
  ChangeDetectorRef, OnDestroy, Inject, PLATFORM_ID, ViewChild, TemplateRef
} from '@angular/core';
import { BreakpointService } from '@dealer-core/services/breakpoint.service';
import { Observable, Subject } from 'rxjs';
import { NzModalRef, NzModalService } from 'ng-zorro-antd/modal';
import { AuthService } from '@dealer-modules/auth/auth.service';
import { UserSignInInfo, UserSignUpInfo } from '@dealer-modules/auth/auth.model';

@Component({
  selector: 'dash-layout-header',
  templateUrl: './layout-header.component.html',
  styleUrls: ['./layout-header.component.scss']
})
export class LayoutHeaderComponent implements OnInit, OnDestroy {
  @ViewChild('signin') public signinRef: TemplateRef<any>;
  @ViewChild('signup') public signUpRef: TemplateRef<any>;

  signInModal: NzModalRef;
  signUpModal: NzModalRef;
  public isVisibleFooterQuickView: boolean;
  public isSearchingMobile: boolean = false;
  public isOpenMenu: boolean = false;
  public isMobile$: Observable<boolean> = this.breakpointService.isMobileDevice;
  private onDestroy$: Subject<boolean> = new Subject<boolean>();
  currentUser: any = null;
  isLogin: boolean = false;

  constructor(
    private readonly breakpointService: BreakpointService,
    private readonly cdr: ChangeDetectorRef,
    private modal: NzModalService,
    private authService: AuthService,
    @Inject(PLATFORM_ID) private readonly platformId: string
  ) {
    this.authService.getCredentialFromStore().subscribe(
      (userInfo) => {
        if (userInfo) {
          this.currentUser = userInfo;
          this.isLogin = true;
        }
      }
    );
  }

  ngOnInit(): void {

  }

  ngOnDestroy() {
    this.onDestroy$.next(true);
    this.onDestroy$.complete();
  }

  /**
   * Toggle show/hide footer quick view area
   *
   * @param isVisible {boolean}
   * @returns {void}
   */
  setVisibleFooterQuickView(isVisible: boolean): void {
    this.isVisibleFooterQuickView = isVisible;
  }

  /**
   * Toggle show/hide for searching area in mobile device
   * @param isVisible {boolean}
   * @returns {void}
   */
  setVisibleSearchingArea(isVisible: boolean): void {
    if (this.isSearchingMobile !== isVisible) {
      this.isSearchingMobile = isVisible;
      this.cdr.markForCheck();
    }
  }

  /**
   * Toggle show/hide for menu in mobile device
   * @param isVisible {boolean}
   * @returns {void}
   */
  setVisibleMenu(isVisible: boolean): void {
    if (this.isOpenMenu !== isVisible) {
      this.isOpenMenu = isVisible;
      this.cdr.markForCheck();
    }
  }

  onSignIn(userSignInInfo: UserSignInInfo) {
    this.authService.login(userSignInInfo).subscribe(
      (userInfo) => {
        this.signInModal.close();
        this.authService.saveCredentialToStore(userInfo).subscribe(
          (userData) => {
            this.currentUser = userData;
            this.isLogin = true;
          }
        );
      }
    );
  }

  onSignUp(userSignUpInfo: UserSignUpInfo) {
    this.authService.register(userSignUpInfo).subscribe(
      (userInfo) => {
        this.currentUser = this.authService.saveCredentialToStore(userInfo);
        this.signUpModal.close();
      }
    );
  }

  showDialogLogin() {
    if (!this.currentUser) {
      this.modal.closeAll();
      this.signInModal = this.modal.create({
        nzContent: this.signinRef,
        nzFooter: null
      });
    }
  }

  showDialogSignup() {
    if (this.currentUser) {
      return;
    }

    this.modal.closeAll();
    this.signUpModal = this.modal.create({
      nzContent: this.signUpRef,
      nzFooter: null
    })
  }

  logOut() {
    this.authService.logout().subscribe(
      () => {
        this.authService.removeCredentialFromStore().subscribe(
          () => {
            this.currentUser = null;
            this.isLogin = false;
          }
        );
      }
    );
  }
}
