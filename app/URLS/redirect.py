from fastapi.responses import RedirectResponse
from app.URLS.dao import LinkDao

from fastapi import APIRouter, Depends

from app.database import get_redis
from app.exceptions import NotFoundLink

router = APIRouter(
    prefix="",
    tags=["Redirect"]
)


async def get_url(short_key:str, redis):
    cached_url = await  redis.get(short_key)
    if cached_url:
        return  cached_url.decode("utf-8")

    link = await  LinkDao.get_one_or_none(short_key=short_key)

    if link:
        await  redis.set(short_key, link.full_url,ex=3600)
        return link.full_url




@router.get("/{short_code}")
async def redirect_to_original(
        short_code:str,
        redis = Depends(get_redis)):

    cached_url = await  redis.get(short_code)

    if cached_url:
        return  RedirectResponse(url=cached_url)

    link = await LinkDao.get_one_or_none(short_key=short_code)

    if not link:
        raise NotFoundLink


    await  redis.set(short_code, link.full_url, ex=3600)

    return  RedirectResponse(url=link.full_url)