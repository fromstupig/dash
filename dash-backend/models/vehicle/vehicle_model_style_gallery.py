from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleModelStyleGallery(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_model_style_galleries'

    vehicle_model_style_id = db.Column(db.Integer, db.ForeignKey('vehicle_model_styles.id'))
    gallery_item_id = db.Column(db.Integer, db.ForeignKey('vehicle_gallery_items.id'))

    gallery_item = db.relationship('VehicleGalleryItem', uselist=False, lazy='joined')
