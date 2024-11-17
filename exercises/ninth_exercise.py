from apis.todo_api import ToDoApi
from models import ToDoModel
from constants import COMMON_URL

from utils import sort_todos_by_date

def ninth_exercise() -> None:
    todo_api = ToDoApi(COMMON_URL)

    todos = todo_api.get_first_page_of_todos(per_page=20)
    todos_model = []

    for todo in todos:
        todos_model.append(ToDoModel(todo))    

    sorted_todos = sort_todos_by_date(todos_model)

    for sorted_todo in sorted_todos:
        print(sorted_todo)
        print("------------")