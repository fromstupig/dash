from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin, MultiTenantMixin


class Country(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'countries'

    name = db.Column(db.String(512), unique=True)
    code = db.Column(db.String(512), unique=True)


class Region(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'regions'

    name = db.Column(db.String(512), unique=True)
    code = db.Column(db.String(512), unique=True)


class State(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'states'

    name = db.Column(db.String(512), unique=True)
    code = db.Column(db.String(512), unique=True)

    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    country = db.relationship('Country', uselist=False, lazy='joined')

    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    region = db.relationship('Region', uselist=False, lazy='joined')


class City(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'cities'

    name = db.Column(db.String(512), unique=True)

    lat = db.Column(db.Float)
    long = db.Column(db.Float)

    state_id = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=True)
    state = db.relationship('State', uselist=False, lazy='joined')

    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=True)
    country = db.relationship('Country', uselist=False, lazy='joined')


class ZipCode(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'zip_codes'

    code = db.Column(db.Integer, unique=True)

    lat = db.Column(db.Float)
    long = db.Column(db.Float)

    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=True)
    city = db.relationship('City', uselist=False, lazy='joined')


class Address(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'addresses'

    raw = db.Column(db.String(2048), unique=True)

    zip_code = db.Column(db.Integer)

    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=True)
    city = db.relationship('City', uselist=False, lazy='joined')

    state_id = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=True)
    state = db.relationship('State', uselist=False, lazy='joined')

    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=True)
    country = db.relationship('Country', uselist=False, lazy='joined')
