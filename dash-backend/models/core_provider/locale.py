from models import db
from models.base import PassivableMixin


class Locale(db.Model, PassivableMixin):
    __tablename__ = 'locales'

    id = db.Column(db.String(2), primary_key=True)
    is_default = db.Column(db.Boolean)
    english_name = db.Column(db.String(10))
