from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleYearModelDriveTrain(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_year_model_drive_trains'

    vehicle_year_model_id = db.Column(db.Integer, db.ForeignKey('vehicle_year_models.id'), nullable=False)

    vehicle_drive_train_id = db.Column(db.Integer, db.ForeignKey('vehicle_drive_trains.id'), nullable=False)
    vehicle_drive_train = db.relationship('VehicleDriveTrain', uselist=False, lazy='joined')
