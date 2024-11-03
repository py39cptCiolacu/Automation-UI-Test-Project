import requests
from typing import TypeVar, Type, List

from constants import USERS_URL, POSTS_URL, TODOS_URL, COMMENTS_URL, API_KEY
from models import User, Post, ToDo, Comment

def create_users() -> list[User]:
    users_response = requests.get(USERS_URL)

    if users_response.status_code != 200:
        raise RuntimeError(f"Something went wrong. Status code: {users_response.status_code}")

    users: list[User] = [User(user_response) for user_response in users_response.json()]
        
    print("***Example for USER***")
    print(users[2])
    print()

    return users   


def create_posts() -> list[Post]:
    posts_response = requests.get(POSTS_URL)
    
    if posts_response.status_code != 200:
        raise RuntimeError(f"Something went wrong. Status code: {posts_response.status_code}")

    posts: list[Post] = [Post(post_response) for post_response in posts_response.json()]
    
    print("***Example for POST***")
    print(posts[0])
    print()

    return posts


def create_todos() -> list[ToDo]:
    todos_response = requests.get(TODOS_URL)
    
    if todos_response.status_code != 200:
        raise RuntimeError(f"Something went wrong. Status code: {todos_response.status_code}")

    todos: list[ToDo] = [ToDo(todo_response) for todo_response in todos_response.json()]

    print("***Example for TODO***")
    print(todos[1])
    print()

    return todos


def create_comments() -> list[Comment]:
    comments_response = requests.get(COMMENTS_URL)

    if comments_response.status_code != 200:
        raise RuntimeError(f"Something went wrong. Status code: {comments_response.status_code}")

    comments: list[Comment] = [Comment(comment_response) for comment_response in comments_response.json()]

    print("***Example for comment***")
    print(comments[0])
    print()

    return comments

T = TypeVar('T')

def create_elements(url: str, element_type: Type[T]) -> List[T]:
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise RuntimeError(f"Something went wrong. Status code: {response.status_code}")
    
    elements: List[T] = [element_type(item) for item in response.json()]

    print(f"***Example for {element_type.__name__}***")
    for element in elements:
        print(element)
        print()

def first_exercise() -> None:
    """
    First way we can do this -  having a function for every type of creation. 
    
    Advantage:
        - if at any point any of each "builder" functions will have different behaviour based on stastus code, or somthing specific, is easier to adapt

    Disadvantage:
        - if we will add 25 more elements, we will repeat the same code again and again
    """
    create_users()
    create_posts()
    create_todos()
    create_comments()

    """"
    Second way in we can do this - having a generic function which takes URL and element type as input

    Advantage:
        - less code, easiser to read and more easy ro scale horizontaly (of we know that we are going to add 25 more elements)
    
    Disdantage:
        - harder to adapt if we need to do also other specific things for specific elements
    """
    create_elements(USERS_URL, User)
    create_elements(POSTS_URL, Post)
    create_elements(TODOS_URL, ToDo)
    create_elements(COMMENTS_URL, Comment)


