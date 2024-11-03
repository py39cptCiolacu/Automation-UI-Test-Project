import requests

from models import User
from constants import USERS_URL, API_KEY


def add_new_user(name: str, email: str, gender: str, status: str) -> User:

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    random_user_dict = {"name": name, 
                        "email": email,
                        "gender": gender,
                        "status": status
                        }

    new_user = requests.post(USERS_URL, headers=headers, json=random_user_dict)
    
    if new_user.status_code != 201:
        raise RuntimeError(f"Status code: {new_user.status_code}. Message : {new_user.text}")
    
    print("The new user had been added succesfuly with the POST request")

    random_user_dict["id"] = new_user.json()["id"]
    new_user_obj = User(info = random_user_dict)
    print(new_user_obj)

    return new_user_obj


def second_exercise() -> None:
    add_new_user(name = "Random Person", email = "email19@email.com", gender = "male", status = "inactive")

