import {
  Component,
  Inject,
  OnDestroy,
  OnInit,
  PLATFORM_ID,
  ViewEncapsulation
} from '@angular/core'
import { NzModalService } from 'ng-zorro-antd/modal'
import { BuildOwnCarComponent } from '../../../../components/modals/build-own-car/build-own-car.component'
import { Observable, of, Subject } from 'rxjs'
import { catchError, map, takeUntil } from 'rxjs/operators'
import { HttpClient } from '@angular/common/http'
import { isPlatformBrowser } from '@angular/common'
import { Router } from '@angular/router'
import { HomeService } from '@dealer-modules/home/services/home.service'

@Component({
  selector: 'dash-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class HomeComponent implements OnInit, OnDestroy {
  public heightScreen = '0px'
  public panels = [
    {
      active: true,
      name:
        'Compete your entire transaction 100% online. Shop for your new car in your PJs?',
      content: `Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint.
                Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet.
                Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint.
                Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet. <br/> <br/>
                Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit.
                Exercitation veniam consequat sunt nostrud amet. Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint.
                Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet.`
    },
    {
      active: false,
      name:
        'Compete your entire transaction 100% online. Shop for your new car in your PJs?',
      content: `Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint.
                Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet.
                Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint.
                Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet. <br/> <br/>
                Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit.
                Exercitation veniam consequat sunt nostrud amet. Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint.
                Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet.`
    },
    {
      active: false,
      name:
        'Compete your entire transaction 100% online. Shop for your new car in your PJs?',
      content: `Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint.
                Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet.
                Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint.
                Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet. <br/> <br/>
                Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit.
                Exercitation veniam consequat sunt nostrud amet. Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint.
                Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet.`
    }
  ]
  public gallery: any[] = []
  public apiLoaded: Observable<boolean>

  private onDestroy$: Subject<boolean> = new Subject<boolean>()

  constructor(
    private modalService: NzModalService,
    private homeServices: HomeService,
    private httpClient: HttpClient,
    private router: Router,
    @Inject(PLATFORM_ID) private readonly platformId: string
  ) {}

  ngOnInit(): void {
    if (isPlatformBrowser(this.platformId)) {
      this.heightScreen = window.innerHeight + 'px'
    }
    this.getVehicleBrands()
    this.initGoogleMap()
  }

  ngOnDestroy(): void {
    this.onDestroy$.next(true)
    this.onDestroy$.complete()
  }

  public openModalBuild() {
    this.modalService.create({
      nzTitle: null,
      nzFooter: null,
      nzWidth: '800px',
      nzStyle: { 'border-radius': '20px' },
      nzContent: BuildOwnCarComponent
    })
  }

  public getVehicleBrands() {
    this.homeServices
      .getVehicleModel()
      .pipe(takeUntil(this.onDestroy$))
      .subscribe((res) => {
        const arrBrands = []
        this.gallery = res.items.filter((item) => {
          if (item.galleries.length && arrBrands.length < 7) {
            arrBrands.push(item.vehicleBrandId)
            return item
          }
        })
      })
  }

  public initGoogleMap() {
    const urlMap =
      'https://maps.googleapis.com/maps/api/js?key=AIzaSyA9qQgUheIXq24gOTuR-cVCz38-vM_qOrE'
    this.apiLoaded = this.httpClient.jsonp(urlMap, 'callback').pipe(
      map(() => true),
      catchError(() => of(false))
    )
  }

  public goToSearchPage(car: any) {
    const url =
      '/searching?branch=' + car['vehicle_brand_id'] + '&model=' + car.id
    this.router.navigateByUrl(url)
    setTimeout((_) => {
      window.scrollTo({ top: 0 })
    })
  }
}
