from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin
from models.vehicle.base import PriceAssignmentMixin


class PriceVehicleModelStyleAssignment(db.Model, IdMixin, CreationTimeMixin, ModificationTimeMixin,
                                       PassivableMixin, PriceAssignmentMixin):
    __tablename__ = 'price_vehicle_model_style_assignments'

    vehicle_model_style_id = db.Column(db.Integer, db.ForeignKey('vehicle_model_styles.id'), nullable=False)
