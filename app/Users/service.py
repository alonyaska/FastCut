from app.Users.auth import get_password_hash, create_access_token, authenticate_user
from app.Users.dao import UsersDao
from app.Users.schemas import SUserRegister, SUserLogin
from app.exceptions import UserAlreadyExistException, UserNotRegistered
from fastapi import  Response


class UserService:

    @classmethod
    async def register_or_401(cls, user_data: SUserRegister):
        existing_user = await UsersDao.get_one_or_none(email=user_data.email)
        if existing_user:
            raise UserAlreadyExistException()
        hashed_password = get_password_hash(user_data.password)
        print(f"DEBUG: password is {hashed_password} type {type(hashed_password)}")
        await  UsersDao.add(email=user_data.email, hashed_password=hashed_password)




    @classmethod
    async  def login_or_401(cls, user_data:SUserLogin, response=Response):
        user = await authenticate_user(email=user_data.email, password=user_data.password)
        if not user:
            raise UserNotRegistered()
        access_token = create_access_token({"sub": str(user.id)})
        response.set_cookie("user_url_token", access_token, httponly=True, secure=False, samesite="lax")
        return access_token



    @classmethod
    async  def logout_user_401(cls, response=Response):
        response.delete_cookie("user_url_token" )