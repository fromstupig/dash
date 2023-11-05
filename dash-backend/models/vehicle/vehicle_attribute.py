from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleAttribute(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_attributes'

    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String, nullable=True)

    parent_id = db.Column(db.Integer, db.ForeignKey('vehicle_attributes.id'), nullable=True)
    parent = db.relationship('VehicleAttribute', remote_side='VehicleAttribute.id', backref='sub_vehicle_attributes')
