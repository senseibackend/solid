from typing import List
from task import Task

class TaskManager:
    """
    Gestiona las tareas y guarda las tareas en un archivo.
    """
    def __init__(self) -> None:
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, task_name: str, user: str) -> None:
        """
        Añade una tarea.
        """
        self.tasks.append(Task(self.next_id, task_name, user))
        self.next_id += 1

    def complete_task(self, task_id: int) -> None:
        """
        Completa una tarea.
        """
        for task in self.tasks:
            if task.id == task_id:
                task.complete()

    def get_tasks(self) -> List[Task]:
        """
        Obtiene todas las tareas.
        """
        return self.tasks
