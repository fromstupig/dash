from sqlalchemy.ext.hybrid import hybrid_property

from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin
from models.vehicle.vehicle_gallery_item import VehicleGalleryItem
from schemas.vehicle.vehicle_gallery_item import vehicle_gallery_item_schema


class VehicleModel(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_models'

    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String, nullable=True)

    vehicle_brand_id = db.Column(db.Integer, db.ForeignKey('vehicle_brands.id'), nullable=False)
    vehicle_brand = db.relationship('VehicleBrand', uselist=False, lazy='joined')

    _galleries = db.relationship('VehicleGalleryItem', secondary='vehicle_model_galleries',
                                 single_parent=True,
                                 cascade='all, delete-orphan')

    @hybrid_property
    def galleries(self):
        return self._galleries

    @galleries.setter
    def galleries(self, value):
        if value is not None:
            self._galleries = list(
                map(lambda item: VehicleGalleryItem(**vehicle_gallery_item_schema.load(item)), value))
