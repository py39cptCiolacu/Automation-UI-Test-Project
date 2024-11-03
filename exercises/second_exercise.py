import requests

from models import User
from constants import USERS_URL, API_KEY

def second_exercise(id: str, name: str, email: str, gender: str, status: str) -> User:

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    random_user_dict = {"id": id, 
                          "name": name, 
                          "email": email,
                          "gender": gender,
                          "status": status
                          }

    new_user = requests.post(USERS_URL, headers=headers, json=random_user_dict)

    if new_user.status_code != 201:
        raise RuntimeError(f"Status code: {new_user.status_code} .Message : {new_user.text}")
    
    print("The new user had been added succesfuly with the POST request")

    new_user_obj = User(random_user_dict)

    print(new_user_obj)


