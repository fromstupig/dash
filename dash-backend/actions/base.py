from models import db


class BaseAction:
    def __init__(self, **kwargs):
        self.db = kwargs.pop('db', db)
        self.model = kwargs.pop('model', self.db.Model)
