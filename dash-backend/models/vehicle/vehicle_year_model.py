import json

from sqlalchemy.ext.hybrid import hybrid_property

from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin
from models.vehicle.vehicle_gallery_item import VehicleGalleryItem

from models.vehicle.vehicle_feature import VehicleDriveTrain, VehicleCategory, VehicleTransmission, VehicleEngine, \
    VehicleInfo
from schemas.vehicle.vehicle_feature import vehicle_transmission_schema, vehicle_engine_schema, vehicle_info_schema
from schemas.vehicle.vehicle_gallery_item import vehicle_gallery_item_schema


class VehicleYearModel(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_year_models'

    name = db.Column(db.String(256), unique=True, nullable=False)
    description = db.Column(db.String, nullable=True)

    year = db.Column(db.Integer(), nullable=False)

    vehicle_model_id = db.Column(db.Integer, db.ForeignKey('vehicle_models.id'), nullable=False)
    vehicle_model = db.relationship('VehicleModel', uselist=False, lazy='joined')

    attributes = db.relationship('VehicleAttributeValue', secondary='vehicle_year_model_attributes')

    _infos = db.relationship('VehicleInfo', secondary='vehicle_year_model_infos', cascade='all')
    _engines = db.relationship('VehicleEngine', secondary='vehicle_year_model_engines', cascade='all')
    _transmissions = db.relationship('VehicleTransmission', secondary='vehicle_year_model_transmissions', cascade='all')

    _drive_trains = db.relationship('VehicleDriveTrain', secondary='vehicle_year_model_drive_trains')
    _categories = db.relationship('VehicleCategory', secondary='vehicle_year_model_categories')

    _galleries = db.relationship('VehicleGalleryItem', secondary='vehicle_year_model_galleries',
                                 single_parent=True,
                                 cascade='all, delete-orphan')

    @hybrid_property
    def drive_trains(self):
        return self._drive_trains

    @drive_trains.setter
    def drive_trains(self, value):
        if value is not None:
            self._drive_trains = VehicleDriveTrain.query \
                .filter(VehicleDriveTrain.id.in_([item['id'] for item in value])).all()

    @hybrid_property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        if value is not None:
            self._categories = VehicleCategory.query \
                .filter(VehicleCategory.id.in_([item['id'] for item in value])).all()

    @hybrid_property
    def transmissions(self):
        return self._transmissions

    @transmissions.setter
    def transmissions(self, value):
        if value is not None:
            self._transmissions = list(
                map(lambda item: VehicleTransmission(**vehicle_transmission_schema.load(item)), value))

    @hybrid_property
    def engines(self):
        return self._engines

    @engines.setter
    def engines(self, value):
        if value is not None:
            self._engines = list(map(lambda item: VehicleEngine(**vehicle_engine_schema.load(item)), value))

    @hybrid_property
    def infos(self):
        return self._infos

    @infos.setter
    def infos(self, value):
        if value is not None:
            self._infos = list(map(lambda item: VehicleInfo(**vehicle_info_schema.load(item)), value))

    @hybrid_property
    def galleries(self):
        return self._galleries

    @galleries.setter
    def galleries(self, value):
        if value is not None:
            self._galleries = list(
                map(lambda item: VehicleGalleryItem(**vehicle_gallery_item_schema.load(item)), value))
