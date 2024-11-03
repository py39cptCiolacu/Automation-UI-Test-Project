import textwrap

class User:
    def __init__(self, info):
        self.id = info["id"]
        self.name = info["name"]
        self.email = info["email"]
        self.gender = info["gender"]
        self.status = info["status"]

    def __str__(self):
        user_text = f"""
                ID: {self.id} 
                NAME: {self.name} 
                EMAIL: {self.email} 
                GENDER: {self.gender} 
                STATUS: {self.status}  
                """
        return textwrap.dedent(user_text).strip()
    
    def user_as_dict(self) -> dict:
        user_dict = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "gender": self.gender,
            "status": self.status
        }

        return user_dict
    
class Post:
    def __init__(self, info):
        self.id = info["id"]
        self.user_id = info["user_id"]
        self.title = info["title"]
        self.body = info["body"]

    def __str__(self):
        post_text = f"""
                    ID: {self.id}
                    USER_ID: {self.user_id}
                    TITLE: {self.title}
                    BODY: {self.body}
                    """

        return textwrap.dedent(post_text).strip()
    
class ToDo: 
    def __init__(self, info):
        self.id = info["id"]
        self.user_id = info["user_id"]
        self.due_on = info["due_on"]
        self.status = info["status"]

    def __str__(self):
        todo_text = f"""
                    ID: {self.id}
                    USER_ID: {self.user_id}
                    DUE ON: {self.due_on}
                    STATUS: {self.status}
                    """

        return textwrap.dedent(todo_text).strip()

class Comment: 
    def __init__(self, info):
        self.id = info["id"]
        self.post_id = info["post_id"]
        self.name = info["name"]
        self.email = info["email"]
        self.body = info["body"]

    def __str__(self):
        todo_text = f"""
                    ID: {self.id}
                    POST_ID: {self.post_id}
                    NAME: {self.name}
                    EMAIL: {self.email}
                    BODY: {self.body}
                    """

        return textwrap.dedent(todo_text).strip()

