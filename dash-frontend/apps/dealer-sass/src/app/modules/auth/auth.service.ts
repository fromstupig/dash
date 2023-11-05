import { Injectable } from '@angular/core';
import { ApiHttpService } from '../../../../../../libs/services/src';
import { Observable, of } from 'rxjs';
import { HttpApiResponseModel } from '../../../../../../libs/types/src';
import { map } from 'rxjs/operators';
import { UserSignUpInfo, UserSignInInfo } from './auth.model';

@Injectable()
export class AuthService {
  constructor(private httpService: ApiHttpService) {
  }

  register(userSignUpInfo: UserSignUpInfo): Observable<any> {
    return this.httpService.post<UserSignUpInfo, HttpApiResponseModel<any>>(`/authentication/_register`, userSignUpInfo).pipe(
      map(data => data.data)
    );
  }

  login(userSignInInfo: UserSignInInfo): Observable<any> {
    return this.httpService.post<UserSignInInfo, HttpApiResponseModel<any>>(`/authentication/_login`, userSignInInfo).pipe(
      map(data => data.data)
    );
  }

  logout(): Observable<any> {
    return this.httpService.post<HttpApiResponseModel<any>>(`/authentication/_logout`, null);
  }

  saveCredentialToStore(userInfo: any): Observable<any> {
    const userInfoAsJsonString = JSON.stringify(userInfo)
    localStorage.setItem("userInfo", userInfoAsJsonString);
    return of(userInfo)
  }

  getCredentialFromStore(): Observable<any> {
    const userInfoAsJsonString = localStorage.getItem("userInfo");
    return of(JSON.parse(userInfoAsJsonString))
  }

  removeCredentialFromStore(): Observable<boolean> {
    localStorage.removeItem("userInfo")
    return of(true)
  }
}
