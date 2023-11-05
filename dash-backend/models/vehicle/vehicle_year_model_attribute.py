from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleYearModelAttribute(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_year_model_attributes'

    vehicle_year_model_id = db.Column(db.Integer, db.ForeignKey('vehicle_year_models.id'), nullable=False)
    vehicle_attribute_value_id = db.Column(db.Integer, db.ForeignKey('vehicle_attribute_values.id'), nullable=False)

    vehicle_attribute_value = db.relationship('VehicleAttributeValue', uselist=False, lazy='joined')
