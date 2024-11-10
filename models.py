import textwrap

class UserModel:
    def __init__(self, info: dict) -> None:
        self.id: str = info.get("id")
        self.name: str = info.get("name")
        self.email: str = info.get("email")
        self.gender: str = info.get("gender")
        self.status: str = info.get("status")

    def __str__(self) -> None:
        user_text = f"""
                ID: {self.id} 
                NAME: {self.name} 
                EMAIL: {self.email} 
                GENDER: {self.gender} 
                STATUS: {self.status}  
                """
        return textwrap.dedent(user_text).strip()

    @classmethod
    def user_model_without_id(cls, name: str, email: str, gender: str, status: str) -> "UserModel":
        data = {"name": name,
                "email": email,
                "gender": gender,
                "status": status}

        return cls(data)

    def update_user_model_id(self, id: str) -> None:
        if self.id:
            raise ValueError("The ID is already defined")
        self.id = id
    
class PostModel:
    def __init__(self, info: dict)-> None:
        self.id = info["id"]
        self.user_id = info["user_id"]
        self.title = info["title"]
        self.body = info["body"]

    def __str__(self) -> str:
        post_text = f"""
                    ID: {self.id}
                    USER_ID: {self.user_id}
                    TITLE: {self.title}
                    BODY: {self.body}
                    """

        return textwrap.dedent(post_text).strip()


class ToDoModel: 
    def __init__(self, info: dict) -> None:
        self.id = info["id"]
        self.user_id = info["user_id"]
        self.due_on = info["due_on"]
        self.status = info["status"]

    def __str__(self) -> str:
        todo_text = f"""
                    ID: {self.id}
                    USER_ID: {self.user_id}
                    DUE ON: {self.due_on}
                    STATUS: {self.status}
                    """

        return textwrap.dedent(todo_text).strip()


class CommentModel: 
    def __init__(self, info: dict)-> None:
        self.id = info["id"]
        self.post_id = info["post_id"]
        self.name = info["name"]
        self.email = info["email"]
        self.body = info["body"]

    def __str__(self) -> str:
        todo_text = f"""
                    ID: {self.id}
                    POST_ID: {self.post_id}
                    NAME: {self.name}
                    EMAIL: {self.email}
                    BODY: {self.body}
                    """

        return textwrap.dedent(todo_text).strip()

