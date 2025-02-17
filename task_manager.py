from typing import List
from task import Task
from task_storage import TextFileStorage, CSVFileStorage

class TaskManager:
    """
    Gestiona las tareas y guarda las tareas en un archivo.
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
    
    def save(self, storage: TextFileStorage | CSVFileStorage) -> None:
        """
        Guarda las tareas en el archivo de texto o CSV.
        """
        storage.save(self.tasks)
