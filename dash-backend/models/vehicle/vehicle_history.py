from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleHistory(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_histories'

    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    purchased_date = db.Column(db.DateTime, nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    owner = db.relationship('User', uselist=False, lazy='joined')

    statuses = db.relationship('VehicleStatus', lazy='joined')
