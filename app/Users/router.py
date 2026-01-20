from fastapi import APIRouter, Response

from app.Users.schemas import SUserRegister, SUserLogin
from app.Users.service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]

)






@router.post("/register")
async def register_user(user_data:SUserRegister):
    return  await UserService.register_or_401(user_data)



@router.post("/login")
async def login_user(user_data:SUserLogin, response:Response):
    return  await UserService.login_or_401(user_data, response)



@router.post("/logout")
async  def logout_user(response:Response):
    return await UserService.logout_user_401(response)