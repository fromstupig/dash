import { Inject, Injectable } from '@angular/core'
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { APP_CONFIG } from '@dash/config'
import { Observable, of } from 'rxjs';

type HttpQueryparams = HttpParams | {
  [param: string]: string | string[];
};

@Injectable({
  providedIn: 'root'
})
export class ApiHttpService {
  private readonly defaultOptions = {
    params: new HttpParams({
      fromObject: {
        direction: 'asc',
        is_active: 'true',
        limit: '100',
        offset: '0',
        sort: 'true'
      }
    })
  }

  constructor(
    @Inject(APP_CONFIG) private appConfig: any,
    private httpClient: HttpClient,
  ) {
  }

  // Can use AuthService in here.
  getHeaders() {
    const userInfoAsJsonString = localStorage.getItem("userInfo");
    const userInfo = JSON.parse(userInfoAsJsonString)
    if(userInfo) {
      return { "authorization" : 'Bearer ' + userInfo.access_token }
    }
  }

  public get<T = any>(path: string, options?: HttpQueryparams): Observable<T> {
    return this.httpClient.get<T>(this.appConfig.apiUrl + path, {params: options ?? this.defaultOptions.params,
      headers: this.getHeaders()});
  }

  public post<T = any, R = any>(path: string, data: T, options?: HttpQueryparams): Observable<R> {
    return this.httpClient.post<R>(this.appConfig.apiUrl + path, data, {params: options ?? this.defaultOptions.params,
      headers: this.getHeaders() });
  }

  public put<T, R>(path: string, data: T, options?: HttpQueryparams): Observable<R> {
    return this.httpClient.put<R>(this.appConfig.apiUrl + path, data, {params: options ?? this.defaultOptions.params,
      headers: this.getHeaders()});
  }

  public delete<R = any>(path: string, options?: HttpQueryparams): Observable<R> {
    return this.httpClient.delete<R>(this.appConfig.apiUrl + path, {params: options ?? this.defaultOptions.params,
      headers: this.getHeaders()});
  }
}

