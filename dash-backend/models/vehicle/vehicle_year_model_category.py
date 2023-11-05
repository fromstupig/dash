from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleYearModelCategory(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_year_model_categories'

    vehicle_year_model_id = db.Column(db.Integer, db.ForeignKey('vehicle_year_models.id'), nullable=False)

    vehicle_category_id = db.Column(db.Integer, db.ForeignKey('vehicle_categories.id'), nullable=False)
    vehicle_category = db.relationship('VehicleCategory', uselist=False, lazy='joined')
