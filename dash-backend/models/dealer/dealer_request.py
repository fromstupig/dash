import enum

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.hybrid import hybrid_property

from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin, MultiTenantMixin
from models.core_provider import Address
from models.dealer.base import MultiDealerMixin
from schemas.core_provider.address import address_schema


class RequestStatus(enum.Enum):
    PENDING = 0
    PROCESSING = 1
    COMPLETED = 2


class DealerRequest(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin, MultiDealerMixin):
    __tablename__ = 'dealer_requests'

    requester_email = db.Column(db.String(128))
    requester_phone_number = db.Column(db.String(32), nullable=False)

    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    vehicle = db.relationship('Vehicle', uselist=False, lazy='joined')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', uselist=False, lazy='joined')

    pricing_detail = db.Column(JSONB, nullable=True)
    credit_information = db.Column(JSONB, nullable=True)
    dealer_option = db.Column(JSONB, nullable=True)

    _address = db.relationship('Address', secondary='requester_addresses',
                               uselist=True,
                               cascade='all, delete')

    status = db.Column(db.Enum(RequestStatus), default=RequestStatus.PENDING)

    @hybrid_property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if value is not None:
            self._address = list(
                map(lambda item: Address(**address_schema.load(item)), value))
