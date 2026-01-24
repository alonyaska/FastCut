import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("email,password,url,short_code,status_code_login, status_code_link",[
    ("123@mail.com","123","https://web.whatsapp.com/", "whatsapp", 200,200),
    ("123@mail.com","123","1231","122133",200, 422)

])



async  def test_create_link(email,password,url, short_code, status_code_login,status_code_link, ac:AsyncClient):
    responce_login = await ac.post("/auth/login", json={
        "email": email,
        "password":password
    })
    assert  responce_login.status_code==status_code_login
    responce_link = await ac.post("/links/shortURL", json={
        "url":url
    },
    params={
        "short_code": short_code
    })
    assert  responce_link.status_code==status_code_link