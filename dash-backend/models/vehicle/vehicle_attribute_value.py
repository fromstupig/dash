from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleAttributeValue(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_attribute_values'

    value = db.Column(db.String, nullable=False)
    value_in_number = db.Column(db.Float, nullable=True)

    vehicle_attribute_id = db.Column(db.Integer, db.ForeignKey('vehicle_attributes.id'), nullable=False)
    vehicle_attribute = db.relationship('VehicleAttribute', uselist=False, lazy='joined')
