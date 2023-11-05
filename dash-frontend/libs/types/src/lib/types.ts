export interface City {
  title: string
  body: string
  timestamp?: Date
}

export interface HttpApiResponseModel<T> {
  data: T;
  success: boolean;
}
