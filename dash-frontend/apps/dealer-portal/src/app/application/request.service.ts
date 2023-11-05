import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { map } from 'rxjs/operators';
import { ApiHttpService } from '../../../../../libs/services/src';
import { HttpApiResponseModel } from '../../../../../libs/types/src';

@Injectable()
export class RequestService {
  constructor(private httpService: ApiHttpService) {
  }

  getRequests(): Observable<any> {
    return this.httpService.get<HttpApiResponseModel<any>>(`/dealer_requests`).pipe(
      map(data => data.data)
    );
  }
}
