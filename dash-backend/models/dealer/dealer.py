from sqlalchemy.ext.hybrid import hybrid_property

from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin, MultiTenantMixin
from models.core_provider import Address
from schemas.core_provider.address import address_schema


class Dealer(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin, MultiTenantMixin):
    __tablename__ = 'dealers'

    name = db.Column(db.String(512), unique=True)
    phone = db.Column(db.String(128), unique=True)
    website = db.Column(db.String(1024), unique=True)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)

    _address = db.relationship('Address', secondary='dealer_addresses', cascade='all, delete')

    @hybrid_property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if value is not None:
            self._address = list(
                map(lambda item: Address(**address_schema.load(item)), value))
