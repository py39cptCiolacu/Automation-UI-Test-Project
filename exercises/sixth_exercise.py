from apis.user_api import UserApi
from models import UserModel
from constants import COMMON_URL

def sixth_exercise() -> None:
    
    user_api = UserApi(COMMON_URL)
    users_with_middle_name =user_api.get_users_with_middle_name(5)

    print(f"Number of users found: {len(users_with_middle_name)}")
    print()

    for user in users_with_middle_name:
        print(UserModel(user))
        print()