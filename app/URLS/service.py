from sqlalchemy.ext.asyncio import AsyncSession

from app.URLS.models import URLsModel
from app.URLS.utils import generate_short_code
from app.exceptions import NotLinkToday


class LinkService:

    @classmethod
    async def create_short_url(cls,short_code:str , url: str, user_id: int, session: AsyncSession):

        if not short_code:
            short_code = generate_short_code()

        new_link = URLsModel(
            full_url=url,
            short_key=short_code,
            user_id=user_id
        )

        try:
            session.add(new_link)
            await session.commit()
            await session.refresh(new_link)
            return new_link
        except Exception:
            await session.rollback()
            raise NotLinkToday




