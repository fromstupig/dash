import enum

from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleGalleryItemType(enum.Enum):
    COVER = 1
    INTERIOR = 2
    INTERIOR_COLOR = 3
    EXTERIOR = 4
    EXTERIOR_COLOR = 5
    BRAND_LOGO = 6
    MODEL_AVATAR = 7
    YEAR_MODEL_AVATAR = 8
    VIDEO_INTRODUCTION = 9
    MODEL_STYLE_AVATAR = 10
    OPTION_ITEM_AVATAR = 11
    VEHICLE_AVATAR = 12
    OTHERS = 99


class VehicleGalleryItem(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_gallery_items'

    type = db.Column(db.Enum(VehicleGalleryItemType), default=VehicleGalleryItemType.OTHERS)
    order = db.Column(db.Integer)
    asset_path = db.Column(db.String)
