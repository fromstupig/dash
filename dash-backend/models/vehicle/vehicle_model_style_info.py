from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleModelStyleInfo(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_model_style_infos'

    vehicle_model_style_id = db.Column(db.Integer, db.ForeignKey('vehicle_model_styles.id'), nullable=False)

    vehicle_info_id = db.Column(db.Integer, db.ForeignKey('vehicle_infos.id'), nullable=False)
    vehicle_info = db.relationship('VehicleInfo', uselist=False, lazy='joined')
