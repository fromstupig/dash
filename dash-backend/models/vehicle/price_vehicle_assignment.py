from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin
from models.vehicle.base import PriceAssignmentMixin


class PriceVehicleAssignment(db.Model, IdMixin, CreationTimeMixin, ModificationTimeMixin, PassivableMixin,
                             PriceAssignmentMixin):
    __tablename__ = 'price_vehicle_assignments'

    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
