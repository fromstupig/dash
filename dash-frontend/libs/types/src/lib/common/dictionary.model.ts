export interface Dictionary<T = any> {
  [key: string]: string | number | boolean | Dictionary | Array<T>;
}
