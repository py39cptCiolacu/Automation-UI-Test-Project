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
    def model_without_id(
        cls, name: str, email: str, gender: str, status: str
    ) -> "UserModel":
        data = {"name": name, "email": email, "gender": gender, "status": status}

        return cls(data)

    def update_id(self, id: str) -> None:
        if self.id:
            raise ValueError("The ID is already defined")
        self.id = id


class PostModel:
    def __init__(self, info: dict) -> None:
        self.id = info.get("id")
        self.user_id = info.get("user_id")
        self.title = info.get("title")
        self.body = info.get("body")

    def __str__(self) -> str:
        post_text = f"""
                    ID: {self.id}
                    USER_ID: {self.user_id}
                    TITLE: {self.title}
                    BODY: {self.body}
                    """

        return textwrap.dedent(post_text).strip()

    @classmethod
    def model_without_id(cls, user_id: str, title: str, body: str) -> "PostModel":
        data = {"user_id": user_id, "title": title, "body": body}

        return cls(data)

    def update_id(self, id: str) -> None:
        if self.id:
            raise ValueError("The ID is already defined")
        self.id = id


class ToDoModel:
    def __init__(self, info: dict) -> None:
        self.id = info.get("id")
        self.user_id = info.get("user_id")
        self.title = info.get("title")
        self.due_on = info.get("due_on")
        self.status = info.get("status")

    def __str__(self) -> str:
        todo_text = f"""
                    ID: {self.id}
                    USER_ID: {self.user_id}
                    TITLE: {self.title}
                    DUE ON: {self.due_on}
                    STATUS: {self.status}
                    """

        return textwrap.dedent(todo_text).strip()

    @classmethod
    def model_without_id(cls, user_id: str, title: str, due_on: str, status: str) -> "ToDoModel":
        data = {"user_id": user_id, "title": title, "due_on": due_on, "status": status}

        return cls(data)

    def update_id(self, id: str) -> None:
        if self.id:
            raise ValueError("The ID is already defined")
        self.id = id


class CommentModel:
    def __init__(self, info: dict) -> None:
        self.id = info.get("id")
        self.post_id = info.get("post_id")
        self.name = info.get("name")
        self.email = info.get("email")
        self.body = info.get("body")

    def __str__(self) -> str:
        todo_text = f"""
                    ID: {self.id}
                    POST_ID: {self.post_id}
                    NAME: {self.name}
                    EMAIL: {self.email}
                    BODY: {self.body}
                    """

        return textwrap.dedent(todo_text).strip()

    @classmethod
    def model_without_id(cls, post_id: str, name: str, email: str, body: str) -> "CommentModel":
        data = {"post_id": post_id, "name": name, "email": email, "body": body}

        return cls(data)

    def update_id(self, id: str) -> None:
        if self.id:
            raise ValueError("The ID is already defined")
        self.id = id   