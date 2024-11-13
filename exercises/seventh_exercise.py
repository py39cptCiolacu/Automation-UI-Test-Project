from apis.post_api import PostApi
from apis.todo_api import ToDoApi
from apis.comment_api import CommentApi
from models import PostModel, ToDoModel, CommentModel
from constants import COMMON_URL


def seventh_exercise() -> None:

    print("Post")
    post_api = PostApi(COMMON_URL)
    random_post = PostModel.model_without_id(
        user_id="7511416", title="Titlu", body="Body"
    )
    post_api.add_post(random_post)
    print(random_post)
    print()

    print("ToDo")
    todo_api = ToDoApi(COMMON_URL)
    random_todo = ToDoModel.model_without_id(
        user_id="7511416",
        title="Random Todo",
        due_on="2024-12-03T00:00:00.000+05:30",
        status="pending",
    )
    todo_api.add_todo(random_todo)
    print(random_todo)
    print()

    print("Comment")
    comment_api = CommentApi(COMMON_URL)
    random_comment = CommentModel.model_without_id(
        post_id="1291",
        name="Gautam Mehra DC",
        email="dc_gautam_mehra@skiles.test",
        body="This is a test comment",
    )
    comment_api.add_comment(random_comment)
    print(random_comment)
    print()
