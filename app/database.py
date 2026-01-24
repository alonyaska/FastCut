from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from  sqlalchemy.orm import  DeclarativeBase, sessionmaker
from app.config import settings
import redis.asyncio as redis


if settings.MODE == "TEST":
    DATABASE_URL = settings.TEST_DATABASE_URL
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = settings.DATABASE_URL
    DATABASE_PARAMS = {}


engine = create_async_engine(settings.DATABASE_URL, **DATABASE_PARAMS)


async_session_maker = async_sessionmaker(
    bind=engine,           # Передаем наш асинхронный движок
    class_=AsyncSession,   # Явно указываем класс сессии
    expire_on_commit=False # Для асинхронности лучше ставить False
)

class Base(DeclarativeBase):
    pass


async def get_async_session():
    async with async_session_maker() as session:
        yield session




async def get_redis():
    client = redis.from_url("redis://localhost:6379", decode_responses=True)
    try:
        yield client
    finally:
        await client.close()