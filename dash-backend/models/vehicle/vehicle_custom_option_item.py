from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleCustomOptionItem(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_custom_option_items'

    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    vehicle_option_item_id = db.Column(db.Integer, db.ForeignKey('vehicle_option_items.id'), nullable=False)

    vehicle_option_item = db.relationship('VehicleOptionItem', lazy='joined')
