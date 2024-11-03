import requests

from constants import USERS_URL, API_KEY
from exercises.second_exercise import add_new_user

def get_actual_number_of_users() -> int:
    
    headers = {
        "Authorization" : f"Bearer {API_KEY}",
    }

    users = requests.get(USERS_URL, headers=headers)
    
    if users.status_code != 200:
        raise RuntimeError(f"Something went wrong. Status code: {users.status_code}")
    
    actual_number_of_users = int(users.headers.get("x-pagination-total"))

    return actual_number_of_users

def check_new_user() -> bool:

    number_of_users_before = get_actual_number_of_users()
    new_user = add_new_user(name="Test Test", email = "test1169@email.com", gender="female", status="inactive")

    if not new_user:
        raise KeyError("This user does not exist!")

    number_of_users_after = get_actual_number_of_users()

    if number_of_users_after-number_of_users_before == 1:
        return True

    print(number_of_users_after)
    print(number_of_users_before)
    
    return False


def third_exercise() -> None:
    """
    - not sure if this type of check is the best, because if 2 servers push a new user at aprox same time, 
    the total number will be increased by 2 - same with deleting (the total number will be same)
    """
    if not check_new_user():
        print("Something went wrong! The user was not added")
        return
    
    print("All good! The new user is there!")