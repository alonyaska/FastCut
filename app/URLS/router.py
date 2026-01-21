
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.URLS.service import LinkService

from app.Users.models import UsersModel
from app.Users.dependencies import get_current_user
from app.database import get_async_session


router = APIRouter(
    prefix="/links",
    tags=["Укоротитель"]
)



router.post("/shortURL")
async def shorten_url(
    url: str,
    user: UsersModel = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):

    new_link = await LinkService.create_short_url(
        url=url,
        user_id=user.id,
        session=session
    )

    return {
        "short_url": f"http://localhost:8000/{new_link.short_key}",
        "original_url": new_link.full_url
    }

