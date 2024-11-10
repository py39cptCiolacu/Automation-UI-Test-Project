from apis.user_api import UserApi
from models import UserModel
from constants import COMMON_URL

def third_exercise() -> None:
    user_api = UserApi(COMMON_URL)

    random_user = UserModel.user_model_without_id(
        name="Random User", email="email99@email.bu", gender="male", status="inactive"
    )

    user_api.add_user(random_user, check_if_was_added=True)
    print(random_user) 