import enum

import bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

from models import db
from models.authorization.reset_token import ResetToken
from models.authorization.role import Role
from models.authorization.session import Session
from models.base import CreationTimeMixin, ModificationTimeMixin, MultiTenantMixin, IdMixin
from utilities.constant import PASSWORD_ENCODING


class UserType(enum.Enum):
    HOST = 1
    TENANT = 2
    EXTERNAL = 3


class User(db.Model, IdMixin, CreationTimeMixin, ModificationTimeMixin, MultiTenantMixin):
    __tablename__ = 'users'

    email = db.Column(db.String(256), unique=True)
    _password = db.Column('password', db.String(128))
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    phone_number = db.Column(db.String(32))
    address = db.Column(db.String(1024))
    title = db.Column(db.String(256))

    google_id = db.Column(db.String(128), nullable=True)
    facebook_id = db.Column(db.String(128), nullable=True)

    type = db.Column(db.Enum(UserType), default=UserType.EXTERNAL)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role', uselist=False, lazy='joined')

    sessions = db.relationship('Session', backref='user', lazy=True)
    reset_token = db.relationship('ResetToken', backref='user', lazy=True)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')

    def verify_password(self, password):
        if self.password is None:
            return False

        return bcrypt.checkpw(password.encode(PASSWORD_ENCODING), self.password.encode(PASSWORD_ENCODING))
