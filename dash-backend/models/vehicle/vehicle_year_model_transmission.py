from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleYearModelTransmission(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_year_model_transmissions'

    vehicle_year_model_id = db.Column(db.Integer, db.ForeignKey('vehicle_year_models.id'), nullable=False)

    vehicle_transmission_id = db.Column(db.Integer, db.ForeignKey('vehicle_transmissions.id'), nullable=False)
    vehicle_transmission = db.relationship('VehicleTransmission', uselist=False, lazy='joined')
