from rest_api_controller import RestApiController
from models import ToDoModel
from apis.user_api import UserApi


class ToDoApi:
    def __init__(self, base_url: str, auth=None) -> None:
        self.controller = RestApiController(base_url, auth)
        self.endpoint = "/todos"

    def get_first_page_of_todos(self, per_page: int) -> list[dict]:
        # TODO: make this return X todos
        return self.controller.get(self.endpoint, params={"per_page": per_page}).json()

    def add_todo(self, todo: ToDoModel) -> None:
        """
        This function will add a new ToDo
        """
        user_api = UserApi(self.controller.base_url)
        if not user_api.__check_user_by_id(todo.user_id):
            return

        response = self.controller.post(
            endpoint=self.endpoint,
            json={
                "user_id": todo.user_id,
                "title": todo.title,
                "due_on": todo.due_on,
                "status": todo.status,
            },
        )

        if response is None:
            print("POST request failed. ToDo was not added")
            return

        todo.update_id(response.json().get("id"))
        print("All good. The new post was added and its ID was updated!")
