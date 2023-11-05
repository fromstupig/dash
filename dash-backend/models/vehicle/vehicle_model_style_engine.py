from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleModelStyleEngine(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_model_style_engines'

    vehicle_model_style_id = db.Column(db.Integer, db.ForeignKey('vehicle_model_styles.id'), nullable=False)

    vehicle_engine_id = db.Column(db.Integer, db.ForeignKey('vehicle_engines.id'), nullable=False)
    vehicle_engine = db.relationship('VehicleEngine', uselist=False, lazy='joined')
