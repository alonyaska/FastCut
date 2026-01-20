from fastapi import HTTPException,status


class InventoryException(HTTPException):
    status_code = 500 # По умолчанию
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class  UserAlreadyExistException(InventoryException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User already registered"


class UserNotRegistered(InventoryException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User not Registered"