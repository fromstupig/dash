from models import db
from models.base import DistributeIdMixin, CreationTimeMixin, ModificationTimeMixin, PassivableMixin, SuspendMixin


class Tenant(db.Model, DistributeIdMixin, CreationTimeMixin, ModificationTimeMixin, PassivableMixin, SuspendMixin):
    __tablename__ = 'tenants'

    name = db.Column(db.String(512), unique=True)
    name_url = db.Column(db.String(512), unique=True)
