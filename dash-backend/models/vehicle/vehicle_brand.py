from sqlalchemy.ext.hybrid import hybrid_property

from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin
from models.vehicle.vehicle_gallery_item import VehicleGalleryItem
from schemas.vehicle.vehicle_gallery_item import vehicle_gallery_item_schema


class VehicleBrand(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_brands'

    name = db.Column(db.String(256), unique=True, nullable=False)
    description = db.Column(db.String, nullable=True)

    _galleries = db.relationship('VehicleGalleryItem', secondary='vehicle_brand_galleries',
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
