from http import HTTPStatus


class ErrorCode:
    DEFAULT = 900
    MISSING_FIELD_EXCEPTION = 901
    INVALID_TOKEN = 902
    NO_VALID_EMAIL = 903
    NO_IP = 904


class DashBaseException(Exception):
    def __init__(self, status_code: int, code=ErrorCode.DEFAULT, detail=None):
        super().__init__(self)

        self.status_code = status_code
        self.code = code
        self.detail = detail

    def to_dict(self):
        return {
            'code': self.code,
            'success': False,
            'detail': self.detail,
            'error': self.__class__.__name__
        }


class UnauthorizedException(DashBaseException):
    def __init__(self, detail=None):
        super().__init__(HTTPStatus.UNAUTHORIZED, detail=detail)


class ForbiddenException(DashBaseException):
    def __init__(self, detail=None):
        super().__init__(HTTPStatus.FORBIDDEN, detail=detail)


class BadRequestException(DashBaseException):
    def __init__(self, code=ErrorCode.DEFAULT, detail=None):
        super().__init__(HTTPStatus.BAD_REQUEST, code, detail)


class MissingFieldException(BadRequestException):
    def __init__(self, field):
        super().__init__(ErrorCode.MISSING_FIELD_EXCEPTION, field)


class EntityNotFoundException(DashBaseException):
    def __init__(self, id, entity: str):
        super().__init__(HTTPStatus.NOT_FOUND, detail={
            'id': id,
            'entity': entity
        })


class DuplicateException(DashBaseException):
    def __init__(self, detail=None):
        super().__init__(HTTPStatus.CONFLICT, detail=detail)


class InternalServerException(DashBaseException):
    def __init__(self, code=ErrorCode.DEFAULT, detail=None):
        super().__init__(HTTPStatus.INTERNAL_SERVER_ERROR, code, detail)


class InvalidRefreshTokenException(UnauthorizedException):
    pass


class InvalidRequestException(Exception):
    def __init__(self, code, status_code=400, detail=None):
        Exception.__init__(self)
        self.code = code
        self.status_code = status_code
        self.detail = detail

    def to_dict(self):
        result = dict(self.detail or ())
        result['code'] = self.code
        return result
