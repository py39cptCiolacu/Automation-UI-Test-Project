
from rest_api_controller import RestApiController
from models import CommentModel
from apis.post_api import PostApi

class CommentApi:
    def __init__(self, base_url: str, auth=None) -> None:
        self.controller = RestApiController(base_url, auth)
        self.endpoint = "/comments"

    def get_first_page_of_comments(self) -> list[dict]:
        return self.controller.get(self.endpoint)
    
    def add_comment(self, comment: CommentModel) -> None:
        """
        This function will add a new Comment
        """
        post_api = PostApi(self.controller.base_url)
        if not post_api.check_post_by_id(comment.post_id):
            return

        response = self.controller.post(
            endpoint=self.endpoint,
            json={
                "post_id": comment.post_id,
                "name": comment.name,
                "email": comment.email,
                "body": comment.body
            }
        )
        if response is None:
            print("POST request failed. Comment was not added")
            return

        comment.update_id(response.json().get("id"))
        print("All good. The new comment was added and its ID was updated!")
        