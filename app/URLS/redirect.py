from fastapi.responses import RedirectResponse
from app.URLS.dao import LinkDao

from fastapi import APIRouter

from app.exceptions import NotFoundLink

router = APIRouter(
    prefix="",
    tags=["Redirect"]
)


@router.get("/{short_code}")
async def redirect_to_original(short_code:str):
    link = await LinkDao.get_one_or_none(short_key=short_code)

    if not link:
        raise NotFoundLink


    return  RedirectResponse(url=link.full_url)