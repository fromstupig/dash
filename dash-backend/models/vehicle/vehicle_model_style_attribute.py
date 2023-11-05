from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleModelStyleAttribute(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_model_style_attributes'

    vehicle_model_style_id = db.Column(db.Integer, db.ForeignKey('vehicle_model_styles.id'), nullable=False)
    vehicle_attribute_value_id = db.Column(db.Integer, db.ForeignKey('vehicle_attribute_values.id'), nullable=False)

    vehicle_attribute_value = db.relationship('VehicleAttributeValue', uselist=False, lazy='joined')
