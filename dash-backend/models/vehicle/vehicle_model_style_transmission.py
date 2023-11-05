from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleModelStyleTransmission(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_model_style_transmissions'

    vehicle_model_style_id = db.Column(db.Integer, db.ForeignKey('vehicle_model_styles.id'), nullable=False)

    vehicle_transmission_id = db.Column(db.Integer, db.ForeignKey('vehicle_transmissions.id'), nullable=False)
    vehicle_transmission = db.relationship('VehicleTransmission', uselist=False, lazy='joined')
