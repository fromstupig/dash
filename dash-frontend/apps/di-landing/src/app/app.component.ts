import { Component, HostListener, Inject, OnInit, PLATFORM_ID } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { isPlatformBrowser } from '@angular/common';
import { NzModalService } from 'ng-zorro-antd/modal';

@Component({
  selector: 'dash-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  public isShowMenuMobile = false;
  public isOnTop = false;
  public formContact: FormGroup;
  public apiContact = 'https://script.google.com/a/angellabstech.com/macros/s/AKfycbyvVtJ1PLtg8RPsf6FMA_a9KwwWDvVA8lWJeazEXQ/exec';
  public heightScreen = '0px';
  public isLoadingForm = false;

  @HostListener('window:scroll')
  private onScroll() {
    if (isPlatformBrowser(this.platformId)) {
      this.isOnTop = window.pageYOffset > 20;
    }
  }

  constructor(private fb: FormBuilder, private httpService: HttpClient, private modalService: NzModalService,
              @Inject(PLATFORM_ID) private readonly platformId: string) {}

  ngOnInit(): void {
    this.buildFormContact();
    if (isPlatformBrowser(this.platformId)) {
      this.heightScreen = window.innerHeight + 'px';
    }
  }

  private buildFormContact() {
    this.formContact = this.fb.group({
      name: [null],
      email: [null, [Validators.required]],
      company: [null],
      phoneNumber: [null],
      message: [null],
    });
  }

  public goToScroll(id) {
    if (isPlatformBrowser(this.platformId)) {
      document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
    }
  }

  public submitForm() {
    console.log(this.formContact);
    if(!this.formContact.invalid) {
      this.isLoadingForm = true;
      this.formContact.disable();
      const data = this.formContact.getRawValue();
      const params = new HttpParams({
        fromObject: {
          name: data.name,
          email: data.email,
          company: data.company,
          phoneNumber: data.phoneNumber,
          message: data.message,
        },
      });
      const httpOptions = {
        headers: new HttpHeaders({
          'Content-Type': 'application/x-www-form-urlencoded',
        }),
      };

      this.httpService.post(this.apiContact, params.toString(), httpOptions).subscribe(res => {
        this.isLoadingForm = false;
        this.formContact.reset();
        this.formContact.enable();
        this.modalService.confirm({
          nzContent: `Thank you, we'll reach out to you soon`,
          nzCancelText: null,
          nzOkText: 'OK'
        });
      });
    }
  }
}
