import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiHttpService } from '../../../../../../libs/services/src';
import { HttpApiResponseModel } from '../../../../../../libs/types/src';
import { map } from 'rxjs/operators';

@Injectable()
export class PaymentService {
  constructor(private httpService: ApiHttpService) {
  }

  getPaymentByDeal(filter: any): Observable<any> {
    return this.httpService.post<HttpApiResponseModel<any>>(`/vehicles/payments`, filter).pipe(
      map(data => data.data.data)
    );
  }

  makeDealerRequest(params: any): Observable<any> {
    return this.httpService.post<HttpApiResponseModel<any>>(`/dealer_requests`, params).pipe(
      map(data => data.data)
    );
  }
}
