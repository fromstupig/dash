from models import db
from models.base import IdMixin, CreationTimeMixin, ModificationTimeMixin


class Session(db.Model, IdMixin, CreationTimeMixin, ModificationTimeMixin):
    __tablename__ = 'sessions'

    token = db.Column(db.String(32), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=True)
