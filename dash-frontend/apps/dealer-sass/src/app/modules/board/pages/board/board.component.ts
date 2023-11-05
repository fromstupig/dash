import { Component, OnDestroy, OnInit, ViewEncapsulation } from '@angular/core';
import { AuthService } from '../../../auth/auth.service';
import { RequestService } from '../../services/request.service';

@Component({
  selector: 'dash-request',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class BoardComponent implements OnInit, OnDestroy {
  currentUser: any;
  requests: [];
  total: number;

  constructor(private authService: AuthService, private requestService: RequestService) {
    this.authService.getCredentialFromStore().subscribe(
      (userInfo) => {
        if(userInfo) {
          this.currentUser = userInfo.user;
          this.requestService.getRequestByCurrentUser().subscribe(
            (requests) => {
              this.total = requests.total;
              this.requests = requests.items;
            }
          )
        }
      }
    )
  }
  ngOnDestroy(): void {
  }

  ngOnInit(): void {
  }

  goToRequestDetail(request_id) {
    console.log(request_id);
  }

  convertDealType(dealType: string) {
    switch (dealType) {
      case "lease" :
        return "Lease";
      case "purchase":
        return "Cash";
      default:
        return "Finance";
    }
  }
}
