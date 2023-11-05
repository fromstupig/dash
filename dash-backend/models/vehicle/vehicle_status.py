from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleStatus(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_statuses'

    checked_date = db.Column(db.DateTime, nullable=False)
    mileage = db.Column(db.Float, nullable=False)
    note = db.Column(db.Text)

    vehicle_history_id = db.Column(db.Integer, db.ForeignKey('vehicle_histories.id'), nullable=False)
