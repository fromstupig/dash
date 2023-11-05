from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleYearModelInfo(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_year_model_infos'

    vehicle_year_model_id = db.Column(db.Integer, db.ForeignKey('vehicle_year_models.id'), nullable=False)

    vehicle_info_id = db.Column(db.Integer, db.ForeignKey('vehicle_infos.id'), nullable=False)
    vehicle_info = db.relationship('VehicleInfo', uselist=False, lazy='joined')
