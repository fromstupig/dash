from sqlalchemy.ext.declarative.base import declared_attr

from models import db


class MultiDealerMixin(object):
    @declared_attr
    def dealer_id(cls):
        return db.Column(db.Integer, db.ForeignKey('dealers.id'), nullable=True)
