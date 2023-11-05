import datetime

from sqlalchemy.ext.declarative import declared_attr

from models import db


class PriceAssignmentMixin(object):
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True)
    value_in_cent = db.Column(db.Integer)

    @declared_attr
    def region_id(cls):
        return db.Column(db.Integer, db.ForeignKey('regions.id'), nullable=True)
