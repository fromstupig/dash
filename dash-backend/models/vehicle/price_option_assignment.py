from models import db
from models.base import CreationTimeMixin, ModificationTimeMixin, IdMixin, PassivableMixin
from models.vehicle.base import PriceAssignmentMixin


class PriceOptionAssignment(db.Model, IdMixin, CreationTimeMixin, ModificationTimeMixin, PassivableMixin,
                            PriceAssignmentMixin):
    __tablename__ = 'price_option_assignments'

    vehicle_option_item_id = db.Column(db.Integer, db.ForeignKey('vehicle_option_items.id'), nullable=False)
