from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleYearModelGallery(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_year_model_galleries'

    vehicle_year_model_id = db.Column(db.Integer, db.ForeignKey('vehicle_year_models.id'))
    gallery_item_id = db.Column(db.Integer, db.ForeignKey('vehicle_gallery_items.id'))

    gallery_item = db.relationship('VehicleGalleryItem', uselist=False, lazy='joined')
