from marshmallow import fields, Schema, post_load

from utilities.exception import DashBaseException


class DashBaseExceptionSchema(Schema):
    __model__ = DashBaseException

    message = fields.String()
    status_code = fields.Integer()

    @post_load
    def make_object(self, data):
        return self.__model__(**data)


dash_base_exception_return_schema = DashBaseExceptionSchema(only=['message', 'status_code'])
