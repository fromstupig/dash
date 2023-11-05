export interface SearchFilterItem {
  value: string;
  text: string;
  type: string;
}
export interface SearchFilter {
  branch?: SearchFilterItem;
  model?: SearchFilterItem;
  year?: SearchFilterItem;
  body?: SearchFilterItem;
  price?: SearchFilterItem;
  color?: SearchFilterItem;
}

export interface SearchFilterData {
  branch?: String;
  model?: String;
  year?: String;
  body?: String;
  price?: String;
  color?: String;
}