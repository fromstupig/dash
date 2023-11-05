import { SearchFilterItem } from './search-filter';

export interface RemoveFilterData {
  all: boolean;
  filter?: SearchFilterItem;
}