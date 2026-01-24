import asyncio
import json
from datetime import datetime

import  pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import insert

from app.config import settings
from  app.database import Base, async_session_maker,engine
from app.Users.models import  UsersModel
from app.URLS.models import URLsModel
from app.main import app


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    assert  settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_json(model:str):
        with open(f"app/tests/to_{model}.json", "r") as file:
            return json.load(file)



    user = open_json("users")
    links = open_json("links")

    for item in links:
        item["created_at"] = datetime.strptime(item["created_at"], "%Y-%m-%d")


    async  with async_session_maker() as session:
        add_users = insert(UsersModel).values(user)
        add_links = insert(URLsModel).values(links)



        await  session.execute(add_users)
        await  session.execute(add_links)

        await  session.commit()
@pytest.fixture(scope="function")
async def ac():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac



@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
