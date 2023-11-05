from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.ext.hybrid import hybrid_property

from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin
from models.vehicle.vehicle_gallery_item import VehicleGalleryItem
from models.vehicle.vehicle_option_item import VehicleOptionItem
from models.vehicle.vehicle_attribute_value import VehicleAttributeValue
from models.vehicle.vehicle_feature import VehicleDriveTrain, VehicleTransmission, VehicleEngine, VehicleInfo
from schemas.vehicle.vehicle_attribute_value import vehicle_attribute_value_schema
from schemas.vehicle.vehicle_feature import vehicle_transmission_schema, vehicle_engine_schema, vehicle_info_schema
from schemas.vehicle.vehicle_gallery_item import vehicle_gallery_item_schema
from schemas.vehicle.vehicle_option_item import vehicle_option_item_schema


class VehicleModelStyle(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_model_styles'

    name = db.Column(db.String(256), unique=True, nullable=False)
    description = db.Column(db.String, nullable=True)

    vif_num = db.Column(db.Integer, nullable=True)

    vehicle_year_model_id = db.Column(db.Integer, db.ForeignKey('vehicle_year_models.id'), nullable=False)
    vehicle_year_model = db.relationship('VehicleYearModel', uselist=False, lazy='joined')

    current_price_assigment = db.relationship('PriceVehicleModelStyleAssignment', uselist=True, lazy='joined')

    include_feature_description = db.Column(db.String)
    style_features = db.Column(ARRAY(db.String), nullable=True)

    standard_feature = db.Column(JSONB, nullable=True)
    technical_feature = db.Column(JSONB, nullable=True)
    consumer_info = db.Column(JSONB, nullable=True)
    pricing_options = db.Column(JSONB, nullable=True)

    base_MSRP = db.Column(db.Float)
    manufacture_code = db.Column(db.String)
    image_url = db.Column(db.String)

    body_id = db.Column(db.Integer, db.ForeignKey('vehicle_bodies.id'))
    body = db.relationship('VehicleBody', lazy='joined')

    _infos = db.relationship('VehicleInfo', secondary='vehicle_model_style_infos', cascade='all')
    _engines = db.relationship('VehicleEngine', secondary='vehicle_model_style_engines')
    _transmissions = db.relationship('VehicleTransmission', secondary='vehicle_model_style_transmissions')
    _drive_trains = db.relationship('VehicleDriveTrain', secondary='vehicle_model_style_drive_trains')

    _options = db.relationship('VehicleOptionItem', secondary='vehicle_model_style_option_items', cascade='all')
    _attributes = db.relationship('VehicleAttributeValue', secondary='vehicle_model_style_attributes', cascade='all')

    _galleries = db.relationship('VehicleGalleryItem', secondary='vehicle_model_style_galleries',
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
    def transmissions(self):
        return self._transmissions

    @transmissions.setter
    def transmissions(self, value):
        if value is not None:
            self._transmissions = VehicleTransmission.query \
                .filter(VehicleTransmission.id.in_([item['id'] for item in value])).all()

    @hybrid_property
    def engines(self):
        return self._engines

    @engines.setter
    def engines(self, value):
        if value is not None:
            self._engines = VehicleEngine.query \
                .filter(VehicleEngine.id.in_([item['id'] for item in value])).all()

    @hybrid_property
    def infos(self):
        return self._infos

    @infos.setter
    def infos(self, value):
        if value is not None:
            self._infos = list(map(lambda item: VehicleInfo(**vehicle_info_schema.load(item)), value))

    @hybrid_property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        if value is not None:
            self._options = list(map(lambda item: VehicleOptionItem(**vehicle_option_item_schema.load(item)), value))

    @hybrid_property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        if value is not None:
            self._attributes = list(
                map(lambda item: VehicleAttributeValue(**vehicle_attribute_value_schema.load(item)), value))

    @hybrid_property
    def galleries(self):
        return self._galleries

    @galleries.setter
    def galleries(self, value):
        if value is not None:
            self._galleries = list(
                map(lambda item: VehicleGalleryItem(**vehicle_gallery_item_schema.load(item)), value))

    __mappings__ = {
        'settings': {
            "index.mapping.total_fields.limit": "2000"
        },
        'mappings': {
            __tablename__: {
                "properties": {
                    "attributes": {
                        "properties": {
                            "creation_date": {
                                "type": "date"
                            },
                            "id": {
                                "type": "long"
                            },
                            "modification_date": {
                                "type": "date"
                            }
                        }
                    },
                    "creation_date": {
                        "type": "date"
                    },
                    "description": {
                        "type": "keyword"
                    },
                    "drive_trains": {
                        "properties": {
                            "creation_date": {
                                "type": "date"
                            },
                            "description": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            },
                            "id": {
                                "type": "long"
                            },
                            "is_active": {
                                "type": "boolean"
                            },
                            "modification_date": {
                                "type": "date"
                            },
                            "name": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            }
                        }
                    },
                    "engines": {
                        "properties": {
                            "creation_date": {
                                "type": "date"
                            },
                            "horse_power": {
                                "type": "long"
                            },
                            "id": {
                                "type": "long"
                            },
                            "is_active": {
                                "type": "boolean"
                            },
                            "label": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            },
                            "modification_date": {
                                "type": "date"
                            },
                            "torque": {
                                "type": "long"
                            },
                            "type": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            }
                        }
                    },
                    "id": {
                        "type": "long"
                    },
                    "include_feature_description": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "modification_date": {
                        "type": "date"
                    },
                    "name": {
                        "type": "keyword"
                    },
                    "options": {
                        "properties": {
                            "creation_date": {
                                "type": "date"
                            },
                            "current_price_assigment": {
                                "properties": {
                                    "creation_date": {
                                        "type": "date"
                                    },
                                    "id": {
                                        "type": "long"
                                    },
                                    "modification_date": {
                                        "type": "date"
                                    },
                                    "region_id": {
                                        "type": "long"
                                    },
                                    "start_date": {
                                        "type": "date"
                                    },
                                    "value_in_cent": {
                                        "type": "long"
                                    },
                                    "vehicle_option_item_id": {
                                        "type": "long"
                                    }
                                }
                            },
                            "description": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            },
                            "detail": {
                                "properties": {
                                    "color": {
                                        "type": "text",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "includes": {
                                        "type": "text",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    }
                                }
                            },
                            "id": {
                                "type": "long"
                            },
                            "is_popular": {
                                "type": "boolean"
                            },
                            "modification_date": {
                                "type": "date"
                            },
                            "type": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            }
                        }
                    },
                    "transmissions": {
                        "properties": {
                            "creation_date": {
                                "type": "date"
                            },
                            "id": {
                                "type": "long"
                            },
                            "is_active": {
                                "type": "boolean"
                            },
                            "label": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            },
                            "modification_date": {
                                "type": "date"
                            },
                            "speeds": {
                                "type": "long"
                            },
                            "type": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            }
                        }
                    },
                    "vehicle_year_model": {
                        "properties": {
                            "description": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            },
                            "name": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            },
                            "vehicle_model": {
                                "properties": {
                                    "description": {
                                        "type": "text",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "name": {
                                        "type": "text",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "vehicle_brand": {
                                        "properties": {
                                            "description": {
                                                "type": "text",
                                                "fields": {
                                                    "keyword": {
                                                        "type": "keyword",
                                                        "ignore_above": 256
                                                    }
                                                }
                                            },
                                            "name": {
                                                "type": "text",
                                                "fields": {
                                                    "keyword": {
                                                        "type": "keyword",
                                                        "ignore_above": 256
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "vehicle_year_model_id": {
                        "type": "long"
                    }
                }
            }
        }
    }
    __search_index__ = __tablename__
    __terms__ = ['vehicle_year_model_id']
    __nested__ = ['vehicle_year_model', 'vehicle_model', 'vehicle_brand']
