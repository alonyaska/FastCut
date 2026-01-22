from fastapi import HTTPException,status


class CutException(HTTPException):
    status_code = 500 # По умолчанию
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class  UserAlreadyExistException(CutException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User already registered"


class UserNotRegistered(CutException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User not Registered"


class UserNotLogin(CutException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User not Login"


class TokenAbsentException(CutException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token is absent"


class TokenIsExpireException(CutException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token is over "


class IncorrectTokenType(CutException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Wrong format token"

class NotLinkToday(CutException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Short key already used"

class NotFoundLink(CutException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Url not found"


