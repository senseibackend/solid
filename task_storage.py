import csv
from typing import List
from task import Task

class TaskStorage:
    """
    Guarda las tareas en un archivo de texto.
    """
    
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def save(self, tasks: List[Task], format: str = "txt") -> None:
        if format == "txt":
            with open(self.filename, "w") as f:
                for task in tasks:
                    f.write(f"{task.id} - {task.name} - {task.user} - {task.completed}\n")
        elif format == "csv":
            with open(self.filename, mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "name", "user", "completed"])
                for task in tasks:
                    writer.writerow([task.id, task.name, task.user, task.completed])
        else: 
            raise ValueError(f"Formato de archivo no válido: {format}")
