from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin, MultiTenantMixin
from models.dealer.base import MultiDealerMixin


class DealerScheduler(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin, MultiDealerMixin):
    __tablename__ = 'dealer_schedulers'

    schedule_title = db.Column(db.String(512))
    schedule_time = db.Column(db.DateTime, nullable=False)
    schedule_note = db.Column(db.Text)

    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    vehicle = db.relationship('Vehicle', uselist=False, lazy='joined')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', uselist=False, lazy='joined')
