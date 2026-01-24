
from httpx import AsyncClient


async  def  test_full_user_path(ac:AsyncClient):


    email = "mytest@mail.ru"
    password = "q12345"
    status_code = 200
    status_code_redirect = 307
    short_code = "alonyatest"
    url = "https://hd.kinogo.fm/218-nevskij-1-7-sezon.html"




    register_response =  await ac.post("/auth/register", json={
        "email": email,
        "password": password
    })
    assert  register_response.status_code == status_code


    login_response = await  ac.post("/auth/login", json={
        "email": email,
        "password": password
    })
    assert  login_response.status_code == status_code


    create_url_response = await ac.post("/links/shortURL", json={
        "url": url
    }, params={
        "short_code":short_code
    })
    assert create_url_response.status_code == 200
    assert create_url_response.json()[1]["short_key"] == short_code

    short_code_now = create_url_response.json()[1]["short_key"]



    check_redirect_response = await ac.get(f"/{short_code_now}")
    assert  check_redirect_response.status_code == status_code_redirect



