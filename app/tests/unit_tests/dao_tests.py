import  pytest

from app.Users.dao import UsersDao



@pytest.mark.parametrize("email,user_id,is_exist",[
    ("123@mail.com",1, True),
    ("1231@mail.com",99, False)
])


async def test_find_by_email(email,user_id, is_exist):
    user = await  UsersDao.find_by_email(email)


    if is_exist:
        assert  user.email == email
        assert user.id == user_id
    else:
        assert  not  user


