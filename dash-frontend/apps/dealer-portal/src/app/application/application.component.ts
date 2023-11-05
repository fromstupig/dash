import { Component, OnInit } from '@angular/core';
import { RequestService } from './request.service';

@Component({
  selector: 'dash-application',
  templateUrl: './application.component.html',
  styleUrls: ['./application.component.scss']
})
export class ApplicationComponent implements OnInit {
  currentUser: any;
  requests: [];
  total: number;

  constructor(private requestService: RequestService) {
  }

  ngOnInit(): void {
    this.requestService.getRequests().subscribe(
      (requests) => {
        this.total = requests.total;
        this.requests = requests.items;
      }
    );
  }

  convertDealType(dealType: string) {
    switch (dealType) {
      case 'lease' :
        return 'Lease';
      case 'purchase':
        return 'Cash';
      default:
        return 'Finance';
    }
  }

  goToRequestDetail(id: number) {
    console.log(id);
  }
}
