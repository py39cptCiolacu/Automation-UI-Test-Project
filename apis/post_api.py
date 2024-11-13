from rest_api_controller import RestApiController
from models import PostModel
from apis.user_api import UserApi

class PostApi:
    def __init__(self, base_url: str, auth=None) -> None:
        self.controller = RestApiController(base_url, auth)
        self.endpoint = "/posts"

    def get_first_page_of_posts(self) -> list[dict]:
        return self.controller.get(self.endpoint)

    def add_post(self, post: PostModel) -> None:
        """
        This function will add a new post
        """
        user_api = UserApi(self.controller.base_url)
        if not user_api.check_user_by_id(post.user_id):
            return

        response = self.controller.post(
            endpoint=self.endpoint,
            json={
                "user_id" : post.user_id,
                "title": post.title,
                "body" : post.body
            },
        )

        if not response.ok:
            print("POST request failed. Post was not added")
            return
        
        post.update_id(response.json().get("id"))
        print("All good. The new post was added and its ID was updated!")
        
    def check_post_by_id(self, id: str) -> bool:
        response = self.controller.get(self.endpoint, params = {"id": id})

        print(type(response.json()))
    
        if response.json() is None:
            return False
        
        return True