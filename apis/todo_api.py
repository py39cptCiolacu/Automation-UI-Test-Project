from rest_api_controller import RestApiController
from models import ToDoModel

class ToDoApi:
    def __init__(self, base_url: str, auth=None) -> None:
        self.controller = RestApiController(base_url, auth)
        self.endpoint = "/todos"

    def get_first_page_of_todos(self) -> list[dict]:
        return self.controller.get(self.endpoint)
