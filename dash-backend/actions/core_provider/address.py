from models.core_provider.address import Country, State, City, ZipCode
from schemas.core_provider.address import country_schema, state_schema, city_schema, countries_schema, states_schema, \
    cities_schema, zip_code_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class CountryAction:
    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = Country.query if q == '' else Country.query.filter(Country.name.like('%{}%'.format(q)))
        query = query.filter(Country.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                Country.name.asc()) if direction == SortDirection.ASC else query.order_by(
                Country.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = countries_schema.dump(items)

        return rv, total


country_action = CountryAction()


class StateAction:
    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = State.query if q == '' else State.query.filter(State.name.like('%{}%'.format(q)))
        query = query.filter(State.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                State.name.asc()) if direction == SortDirection.ASC else query.order_by(
                State.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = states_schema.dump(items)

        return rv, total

    def get_all_by_country_id(self, country_id, sort, direction, limit, offset, is_active, q=''):
        query = State.query if q == '' else State.query.filter(State.name.like('%{}%'.format(q)))
        query = query.filter(State.is_active == is_active) if is_active is not None else query
        query = query.filter(State.country_id == country_id)

        if sort:
            query = query.order_by(
                State.name.asc()) if direction == SortDirection.ASC else query.order_by(
                State.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = states_schema.dump(items)

        return rv, total


state_action = StateAction()


class CityAction:
    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = City.query if q == '' else City.query.filter(City.name.like('%{}%'.format(q)))
        query = query.filter(City.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                City.name.asc()) if direction == SortDirection.ASC else query.order_by(
                City.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = cities_schema.dump(items)

        return rv, total

    def get_all_by_state_id(self, state_id, sort, direction, limit, offset, is_active, q=''):
        query = City.query if q == '' else City.query.filter(City.name.like('%{}%'.format(q)))
        query = query.filter(City.is_active == is_active) if is_active is not None else query
        query = query.filter(City.state_id == state_id)

        if sort:
            query = query.order_by(
                City.name.asc()) if direction == SortDirection.ASC else query.order_by(
                City.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = cities_schema.dump(items)

        return rv, total


city_action = CityAction()


class ZipCodeAction:
    def get_by_zip_code(self, zip_code):
        zip_code_entity = ZipCode.query.filter(ZipCode.is_active).filter(ZipCode.code == zip_code).first()

        if zip_code_entity is None:
            raise EntityNotFoundException(zip_code, 'ZipCode')
        else:
            return zip_code_schema.dump(zip_code_entity)


zip_code_action = ZipCodeAction()
