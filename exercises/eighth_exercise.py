from apis.user_api import UserApi
from models import UserModel
from constants import COMMON_URL


def eighth_exercise() -> None:
    user_api = UserApi(COMMON_URL)
    chosen_user_id = "752asd"
    user_api.change_email_address(user_id=chosen_user_id, new_email_address="test6000@test.com")

