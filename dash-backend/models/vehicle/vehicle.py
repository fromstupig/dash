from sqlalchemy.ext.hybrid import hybrid_property

from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin
from models.vehicle.vehicle_option_item import VehicleOptionItem
from models.vehicle.vehicle_gallery_item import VehicleGalleryItem
from schemas.vehicle.vehicle_gallery_item import vehicle_gallery_item_schema
from schemas.vehicle.vehicle_option_item import vehicle_option_item_schema


class Vehicle(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicles'

    description = db.Column(db.String, nullable=True)
    is_pre_owned = db.Column(db.Boolean, default=False)

    vehicle_brand_id = db.Column(db.Integer, db.ForeignKey('vehicle_brands.id'), nullable=False)
    vehicle_brand = db.relationship('VehicleBrand', uselist=False, lazy='joined')

    vehicle_model_id = db.Column(db.Integer, db.ForeignKey('vehicle_models.id'), nullable=False)
    vehicle_model = db.relationship('VehicleModel', uselist=False, lazy='joined')

    vehicle_model_style_id = db.Column(db.Integer, db.ForeignKey('vehicle_model_styles.id'), nullable=False)
    vehicle_model_style = db.relationship('VehicleModelStyle', uselist=False, lazy='joined')

    current_owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    current_owner = db.relationship('User', uselist=False, lazy='joined')

    current_price_assigment = db.relationship('PriceVehicleAssignment', uselist=False, lazy='joined')
    custom_attributes = db.relationship('VehicleCustomAttribute', uselist=True, lazy='joined')
    _custom_options = db.relationship('VehicleOptionItem', secondary='vehicle_custom_option_items', uselist=True,
                                      lazy='joined')
    histories = db.relationship('VehicleHistory', uselist=True, lazy='joined')

    _galleries = db.relationship('VehicleGalleryItem', secondary='vehicle_galleries',
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
    def custom_options(self):
        return self._custom_options

    @custom_options.setter
    def custom_options(self, value):
        if value is not None:
            self._custom_options = list(
                map(lambda item: VehicleOptionItem(**vehicle_option_item_schema.load(item)), value))

    __mappings__ = {
        'settings': {
            "index.mapping.total_fields.limit": "2000"
        },
        'mappings': {
            __tablename__: {
                "properties": {
                    "custom_options": {
                        "type": "nested"
                    },
                    "vehicle_model_style": {
                        "type": "nested",
                        "properties": {
                            "technical_feature": {
                                "type": "text"
                            },
                            "standard_feature": {
                                "type": "text"
                            },
                            "consumer_info": {
                                "type": "text"
                            },
                            "pricing_options": {
                                "type": "text"
                            },

                        }
                    }
                }
            }
        }
    }
    __search_index__ = __tablename__
    __terms__ = []
    __nested__ = ['vehicle_model_style', 'vehicle_model', 'vehicle_brand']
