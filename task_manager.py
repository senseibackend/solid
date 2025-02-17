from typing import List
from task import Task
from task_storage import IDBStorage, IFileStorage

class TaskManager:
    """
    Gestiona las tareas y guarda las tareas en un almacenamiento.
    """
    def __init__(self) -> None:
        self.tasks: List[Task] = []
        self.next_id: int = 1
    
    def add_task(self, task_name: str, user: str) -> None:
        self.tasks.append(Task(self.next_id, task_name, user))
        self.next_id += 1

    def complete_task(self, task_id: int) -> None:
        for task in self.tasks:
            if task.id == task_id:
                task.complete()

    def get_tasks(self) -> List[Task]:
        return self.tasks
    
    def save(self, storage: IDBStorage | IFileStorage) -> None:
        storage.save(self.tasks)
