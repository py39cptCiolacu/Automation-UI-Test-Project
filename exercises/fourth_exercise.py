from models import User

def fourth_exercise() -> None:
    user_id = User.get_user_id_by_name("Random Person")
    print(user_id)