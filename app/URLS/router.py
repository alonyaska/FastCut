
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.URLS.service import LinkService
from app.URLS.shemas import SLinkCreate

from app.Users.models import UsersModel
from app.Users.dependencies import get_current_user
from app.database import get_async_session


router = APIRouter(
    prefix="/links",
    tags=["Укоротитель"]
)



@router.post("/shortURL")
async def shorten_url(
    short_code:str = Query(None, description="Введите свой кастомный ключ"),
    data: SLinkCreate = None, #
    user: UsersModel = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):

    new_link = await LinkService.create_short_url(
        url=str(data.url),
        user_id=user.id,
        session=session,
        short_code=short_code
    )


    return {"short_url": f"http://localhost:8000/{new_link.short_key}"}, new_link

