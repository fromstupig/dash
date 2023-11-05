from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin, MultiTenantMixin
from models.dealer.base import MultiDealerMixin


class DealerAddress(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin, MultiDealerMixin):
    __tablename__ = 'dealer_addresses'

    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    address = db.relationship('Address', uselist=False, lazy='joined')
