from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin
from models.dealer.base import MultiDealerMixin


class RequesterAddress(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin, MultiDealerMixin):
    __tablename__ = 'requester_addresses'

    dealer_request_id = db.Column(db.Integer, db.ForeignKey('dealer_requests.id'))

    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    address = db.relationship('Address', uselist=False, lazy='joined')
