import pytest
from  httpx import AsyncClient



@pytest.mark.parametrize("email,password,status_code", [
    ("alonyatest@mail.ru","124567", 200),
    ("alonyatest2@mail.ru","124314567", 200),
    ("alonyatest3@mail.ru","12456hrthg7", 200)
])


async def test_register(email,password, status_code, ac:AsyncClient):
    response = await  ac.post("/auth/register", json={
        "email": email,
        "password": password
    })
    assert  response.status_code == status_code



@pytest.mark.parametrize("email, password,status_code",[
    ("123@mail.com", "123", 200),
    ("lol@mial.com", "12131", 401)

])


async def test_login(email,password,status_code, ac:AsyncClient):
    response = await ac.post("/auth/login", json={
        "email":email,
        "password":password
    })
    assert  response.status_code == status_code
