import enum

from sqlalchemy.ext.hybrid import hybrid_property

from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class EngineType(enum.Enum):
    OTHERS = 0
    GAS = 1
    DIESEL = 2
    ELECTRIC = 3


class VehicleEngine(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_engines'

    label = db.Column(db.String(256))
    horse_power = db.Column(db.Integer)
    torque = db.Column(db.Integer)
    type = db.Column(db.Enum(EngineType), default=EngineType.OTHERS)


class TransmissionType(enum.Enum):
    OTHERS = 0
    AUTOMATIC = 1
    MANUAL = 2


class VehicleTransmission(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_transmissions'

    label = db.Column(db.String(256))
    speeds = db.Column(db.Integer)
    type = db.Column(db.Enum(TransmissionType), default=TransmissionType.OTHERS)


class VehicleDriveTrain(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_drive_trains'

    name = db.Column(db.String(256), unique=True, nullable=False)
    description = db.Column(db.String, nullable=True)


class VehicleCategory(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_categories'

    name = db.Column(db.String(256), unique=True, nullable=False)
    description = db.Column(db.String, nullable=True)


class VehicleBody(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_bodies'

    name = db.Column(db.String(256), unique=True, nullable=False)
    description = db.Column(db.String, nullable=True)


class VehicleWarranty(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_warranties'

    vehicle_info_id = db.Column(db.Integer, db.ForeignKey('vehicle_infos.id'))

    comprehensive = db.Column(db.String())
    power_train = db.Column(db.String())
    anti_corrosion = db.Column(db.String())
    paint = db.Column(db.String())
    roadside_assistance = db.Column(db.String())


class VehicleInfo(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_infos'

    description = db.Column(db.Text)

    city_mpg = db.Column(db.Integer)
    combined_mpg = db.Column(db.Integer)
    highway_mpg = db.Column(db.Integer)

    safety_rate = db.Column(db.Integer)

    doors = db.Column(db.Integer)
    seats = db.Column(db.Integer)

    _vehicle_warranty = db.relationship('VehicleWarranty', uselist=False, lazy='joined', cascade='all, delete')

    @hybrid_property
    def vehicle_warranty(self):
        return self._vehicle_warranty

    @vehicle_warranty.setter
    def vehicle_warranty(self, value):
        if value is not None:
            self._vehicle_warranty = VehicleWarranty(**value)
