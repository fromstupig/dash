from marshmallow import fields

from models.core_provider import Address, City, State, Country
from models.core_provider.address import ZipCode, Region
from schemas.base import IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema


class CountrySchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema):
    __model__ = Country

    name = fields.String()
    code = fields.String()


country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)


class RegionSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema):
    __model__ = Region

    name = fields.String()
    code = fields.String()


region_schema = RegionSchema()
regions_schema = RegionSchema(many=True)


class StateSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema):
    __model__ = State

    name = fields.String()
    code = fields.String()

    country_id = fields.Integer()
    country = fields.Nested(CountrySchema, many=False)

    region_id = fields.Integer()
    region = fields.Nested(RegionSchema, many=False)


state_schema = StateSchema()
states_schema = StateSchema(many=True)


class CitySchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema):
    __model__ = City

    name = fields.String()

    lat = fields.Float()
    long = fields.Float()

    state_id = fields.Integer()
    state = fields.Nested(StateSchema, many=False)

    country_id = fields.Integer()
    country = fields.Nested(CountrySchema, many=False)


city_schema = CitySchema()
cities_schema = CitySchema(many=True)


class ZipCodeSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema):
    __model__ = ZipCode

    code = fields.Integer()

    lat = fields.Float()
    long = fields.Float()

    city_id = fields.Integer()
    city = fields.Nested(CitySchema, many=False)


zip_code_schema = ZipCodeSchema()
zip_codes_schema = ZipCodeSchema(many=True)


class AddressSchema(IdSchema, CreationTimeSchema, ModificationTimeSchema, PassivableSchema):
    __model__ = Address

    raw = fields.String()

    zip_code = fields.Integer()

    city_id = fields.Integer()
    city = fields.Nested(CitySchema, many=False)

    state_id = fields.Integer()
    state = fields.Nested(StateSchema, many=False)

    country_id = fields.Integer()
    country = fields.Nested(CountrySchema, many=False)


address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)
