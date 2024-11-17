from datetime import datetime
from models import ToDoModel

def sort_todos_by_date(todos: list[ToDoModel], reverse: bool = False) -> list:
    
    return sorted(
        todos,
        key = lambda todo: datetime.fromisoformat(todo.due_on),
        reverse = reverse
    )