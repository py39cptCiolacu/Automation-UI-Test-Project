
from rest_api_controller import RestApiController
from models import CommentModel

class CommentApi:
    def __init__(self, base_url: str, auth=None) -> None:
        self.controller = RestApiController(base_url, auth)
        self.endpoint = "/comments"

    def get_first_page_of_comments(self) -> list[dict]:
        return self.controller.get(self.endpoint)
