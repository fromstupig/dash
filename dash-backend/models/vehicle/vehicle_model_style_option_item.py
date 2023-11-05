from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleModelStyleOptionItem(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_model_style_option_items'

    vehicle_model_style_id = db.Column(db.Integer, db.ForeignKey('vehicle_model_styles.id'), nullable=False)
    vehicle_option_item_id = db.Column(db.Integer, db.ForeignKey('vehicle_option_items.id'), nullable=False)

    vehicle_option_item = db.relationship('VehicleOptionItem', uselist=False, lazy='joined')
