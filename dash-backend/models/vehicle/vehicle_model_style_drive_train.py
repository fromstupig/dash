from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin


class VehicleModelStyleDriveTrain(db.Model, CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin):
    __tablename__ = 'vehicle_model_style_drive_trains'

    vehicle_model_style_id = db.Column(db.Integer, db.ForeignKey('vehicle_model_styles.id'), nullable=False)

    vehicle_drive_train_id = db.Column(db.Integer, db.ForeignKey('vehicle_drive_trains.id'), nullable=False)
    vehicle_drive_train = db.relationship('VehicleDriveTrain', uselist=False, lazy='joined')
