import json

import click
from flask.cli import AppGroup, with_appcontext

from models import db
from models.core_provider.address import Country, State, City, ZipCode, Region

core_provider_cli = AppGroup('core_provider', help='Core Provider data')


@core_provider_cli.command('countries', help='Seed countries data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_countries(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        countries_list = json.load(json_file)
        for country_data in countries_list:
            is_exists = len(Country.query.filter(Country.code == country_data['code']).all()) > 0
            if is_exists:
                print(str(country_data['code']) + ' is exists.')
            else:
                db.session.add(Country(**country_data))
        db.session.commit()


@core_provider_cli.command('regions', help='Seed regions data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_regions(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        regions_list = json.load(json_file)
        for region_data in regions_list:
            is_exists = len(Region.query.filter(Region.code == region_data['code']).all()) > 0
            if is_exists:
                print(str(region_data['code']) + ' is exists.')
            else:
                db.session.add(Region(**region_data))
        db.session.commit()


@core_provider_cli.command('states', help='Seed states data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_states(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        states_list = json.load(json_file)
        us_country = Country.query.filter(Country.code == 'US').first()
        regions = Region.query.all()
        # northeast = ["ME", "NH", "MA", "VT", "RI", "CT", "NY", "PA", "NJ"]
        # midwest = ["ND", "SD", "NE", "KS", "MN", "IA", "MO", "WI", "IL", "IN", "MI", "OH"]
        # south = ["OK", "TX", "AR", "LA", "MS", "KY", "TN", "AL", "WV", "VA", "NC", "SC", "GA", "FL", "DE", "MD", "DC"]
        # west = ["WA", "OR", "CA", "NV", "ID", "UT", "AZ", "MT", "WY", "CO", "NM", "AK", "HI"]
        for state_data in states_list:
            is_exists = len(State.query.filter(State.code == state_data['code']).all()) > 0
            if is_exists:
                print(str(state_data['code']) + ' is exists.')
            else:
                region_data = list(filter(lambda region: region.code == state_data['region'], regions))
                state_data['region_id'] = region_data[0].id if len(region_data) > 0 else None
                state_data['country_id'] = us_country.id
                del state_data['region']
                db.session.add(State(**state_data))
        db.session.commit()


@core_provider_cli.command('cities', help='Seed cities data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_cities(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        cities_list = json.load(json_file)
        us_country = Country.query.filter(Country.code == 'US').first()
        for city_data in cities_list:
            if city_data['state'] in ['AA', 'AE', 'AP']:
                pass
            else:
                is_exists = len(City.query.filter(City.name == city_data['city']).all()) > 0
                if is_exists:
                    pass
                    # print(str(city_data['city']) + ' is exists.')
                else:
                    state = State.query.filter(State.code == city_data['state']).first()
                    if state is not None:
                        city = dict(
                            name=city_data['city'],
                            lat=city_data['lat'],
                            long=city_data['long'],
                            state_id=state.id,
                            country_id=us_country.id
                        )
                        db.session.add(City(**city))
                    else:
                        print(
                            'There is no state name ' + str(city_data['state']) + ' for city ' + str(city_data['city'])
                            + ' is exists.')
        db.session.commit()


@core_provider_cli.command('zip_codes', help='Seed zip_codes data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_zip_codes(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        zip_codes_list = json.load(json_file)
        for zip_codes_data in zip_codes_list:
            if zip_codes_data['state'] in ['AA', 'AE', 'AP']:
                pass
            else:
                is_exists = len(ZipCode.query.filter(ZipCode.code == zip_codes_data['zip_code']).all()) > 0
                if is_exists:
                    pass
                    # print(str(zip_codes_data['zip_code']) + ' is exists.')
                else:
                    city = City.query.filter(City.name == zip_codes_data['city']).first()
                    if city is not None:
                        zip_code = dict(
                            code=zip_codes_data['zip_code'],
                            lat=zip_codes_data['lat'],
                            long=zip_codes_data['long'],
                            city_id=city.id,
                        )
                        db.session.add(ZipCode(**zip_code))
                    else:
                        print('There is no city name ' + str(zip_codes_data['city']) + ' for zip code '
                              + str(zip_codes_data['zip_code']) + ' is exists.')
        db.session.commit()