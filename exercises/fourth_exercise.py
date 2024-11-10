from apis.user_api import UserApi
from constants import COMMON_URL

def fourth_exercise() -> None:
    user_api = UserApi(COMMON_URL)

    user_id = user_api.get_user_id_by_name("Random Person")
    print(f"ID: {user_id}")