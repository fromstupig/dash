from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleYearModelEngine(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_year_model_engines'

    vehicle_year_model_id = db.Column(db.Integer, db.ForeignKey('vehicle_year_models.id'), nullable=False)

    vehicle_engine_id = db.Column(db.Integer, db.ForeignKey('vehicle_engines.id'), nullable=False)
    vehicle_engine = db.relationship('VehicleEngine', uselist=False, lazy='joined')
