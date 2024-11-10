from apis.user_api import UserApi
from models import UserModel
from constants import COMMON_URL

def fifth_exercise() -> None:
    user_api = UserApi(COMMON_URL)
    active_users = user_api.get_users_by_status(20, "active")

    i = 0
    for active_user in active_users:
        print(f"User number {i}")
        print(UserModel(active_user))
        print()
        i+=1