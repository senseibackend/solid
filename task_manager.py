import csv
from typing import List, Dict, Union

class TaskManager:
    """
    Gestiona las tareas y guarda las tareas en un archivo.
    """
    
    def __init__(self) -> None:
        self.tasks: List[Dict[str, Union[int, str, bool]]] = []
        self.next_id: int = 1

    def add_task(self, task_name: str, user: str) -> None:
        task: Dict[str, Union[int, str, bool]] = {
            "id": self.next_id,
            "name": task_name,
            "user": user,
            "completed": False
        }
        self.tasks.append(task)
        self.next_id += 1

    def complete_task(self, task_id: int) -> None:
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True

    def get_tasks(self) -> List[Dict[str, Union[int, str, bool]]]:
        return self.tasks

    def save(self, format: str = "txt", filename: str = "tasks.txt") -> None:
        if format == "txt":
            with open(filename, "w") as f:
                for task in self.tasks:
                    f.write(f"{task.get('id')} - {task.get('name')} - {task.get('user')} - {task.get('completed')}\n")
        elif format == "csv":
            with open(filename, mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "name", "user", "completed"])
                for task in self.tasks:
                    writer.writerow([task.get('id'), task.get('name'), task.get('user'), task.get('completed')])
        else: 
            raise ValueError(f"Formato de archivo no válido: {format}")
