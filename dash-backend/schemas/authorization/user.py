from marshmallow import post_load, fields, EXCLUDE
from marshmallow_enum import EnumField

from models.authorization.user import User, UserType
from schemas.base import IdSchema


class UserSchema(IdSchema):
    class Meta:
        unknown = EXCLUDE

    email = fields.Email(required=True)
    password = fields.String(load_only=True)
    first_name = fields.String(required=True, data_key='firstName')
    last_name = fields.String(required=True, data_key='lastName')
    phone_number = fields.String()
    avatar_url = fields.String()
    address = fields.String()
    title = fields.String()

    google_id = fields.String()
    facebook_id = fields.String()

    type = EnumField(UserType, by_value=True)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
update_user_schema = UserSchema()
user_profile_schema = UserSchema(exclude=['google_id', 'facebook_id'])
