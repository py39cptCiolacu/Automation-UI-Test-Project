import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
USERS_URL = "https://gorest.co.in/public/v2/users"
POSTS_URL = "https://gorest.co.in/public/v2/posts"
COMMENTS_URL = "https://gorest.co.in/public/v2/comments"
TODOS_URL = "https://gorest.co.in/public/v2/todos"