
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.URLS.service import LinkService
from app.URLS.shemas import SLinkCreate, SLink

from app.Users.models import UsersModel
from app.Users.dependencies import get_current_user
from app.database import get_async_session


router = APIRouter(
    prefix="/links",
    tags=["Укоротитель"]
)



@router.post("/shortURL", response_model=SLink)
async def shorten_url(
    data: SLinkCreate, #
    user: UsersModel = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):

    new_link = await LinkService.create_short_url(
        url=str(data.url),
        user_id=user.id,
        session=session
    )


    return new_link
