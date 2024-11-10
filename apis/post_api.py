from rest_api_controller import RestApiController
from models import PostModel

class PostApi:
    def __init__(self, base_url: str, auth=None) -> None:
        self.controller = RestApiController(base_url, auth)
        self.endpoint = "/posts"

    def get_first_page_of_posts(self) -> list[dict]:
        return self.controller.get(self.endpoint)
