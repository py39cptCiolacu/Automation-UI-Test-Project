from apis.user_api import UserApi
from apis.todo_api import ToDoApi
from apis.post_api import PostApi
from apis.comment_api import CommentApi

from models import UserModel, PostModel, ToDoModel, CommentModel

from constants import COMMON_URL

def first_exercise() -> None:

    user_api = UserApi(COMMON_URL)
    first_page_of_users = user_api.get_first_page_of_users()
    random_user = UserModel(info = first_page_of_users[0])
    print(random_user)
    print() 

    todo_api = ToDoApi(COMMON_URL)
    first_page_of_todos = todo_api.get_first_page_of_todos()
    random_todo = ToDoModel(info = first_page_of_todos[0])
    print(random_todo)
    print()

    post_api = PostApi(COMMON_URL)
    first_page_of_posts = post_api.get_first_page_of_posts()
    random_post = PostModel(info = first_page_of_posts[0])
    print(random_post)
    print()

    comment_api = CommentApi(COMMON_URL)
    first_page_of_comments = comment_api.get_first_page_of_comments()
    random_comment = CommentModel(info = first_page_of_comments[0])
    print(random_comment)
