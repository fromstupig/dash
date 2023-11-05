from sqlalchemy.ext.hybrid import hybrid_property

from models import db
from models.base import IdMixin, CreationTimeMixin, ModificationTimeMixin


class MediaResource(db.Model, CreationTimeMixin, ModificationTimeMixin):
    __tablename__ = 'media_resources'

    public_id = db.Column(db.String(256), primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('media_providers.id'))
    format = db.Column(db.String(10))

    def __repr__(self):
        return '<{} with pulic_id {}>'.format(self.__tablename__, self.public_id)


class MediaProvider(db.Model, IdMixin, CreationTimeMixin, ModificationTimeMixin):
    __tablename__ = 'media_providers'

    _resources = db.relationship('MediaResource', cascade='all,delete', lazy='subquery')

    @hybrid_property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, value):
        if value is not None:
            self._resources = list(map(lambda item: MediaResource(**item), value))
