import enum

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.hybrid import hybrid_property

from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin
from models.vehicle import PriceOptionAssignment
from models.vehicle.vehicle_gallery_item import VehicleGalleryItem
from schemas.vehicle.price_option_assignment import price_option_assignment_schema
from schemas.vehicle.vehicle_gallery_item import vehicle_gallery_item_schema


class VehicleOptionGroupType(enum.Enum):
    INTERIOR_COLOR = 1
    EXTERIOR_COLOR = 2
    PACKAGE = 3
    OPTION = 4
    OTHERS = 99


class VehicleOptionItem(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_option_items'

    description = db.Column(db.String, nullable=False)
    detail = db.Column(JSONB, nullable=True)
    is_popular = db.Column(db.Boolean, default=False)
    type = db.Column(db.Enum(VehicleOptionGroupType), default=VehicleOptionGroupType.OTHERS)

    _current_price_assigment = db.relationship('PriceOptionAssignment',
                                               uselist=True, lazy='joined',
                                               cascade='all, delete-orphan')

    _galleries = db.relationship('VehicleGalleryItem', secondary='vehicle_option_item_galleries',
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

    @hybrid_property
    def current_price_assigment(self):
        return self._current_price_assigment

    @current_price_assigment.setter
    def current_price_assigment(self, value):
        if value is not None:
            self._current_price_assigment = list(
                map(lambda item: PriceOptionAssignment(**item), value))
