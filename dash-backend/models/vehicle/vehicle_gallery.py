from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleGallery(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_galleries'

    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    gallery_item_id = db.Column(db.Integer, db.ForeignKey('vehicle_gallery_items.id'))

    gallery_item = db.relationship('VehicleGalleryItem', uselist=False, lazy='joined')
