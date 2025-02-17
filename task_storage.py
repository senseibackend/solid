from abc import ABC, abstractmethod
import csv
from typing import List
from task import Task

class IFileStorage(ABC):
    """
    Guarda las tareas en un archivo.
    """

    def __init__(self, filename: str) -> None:
        self.filename = filename

    @abstractmethod
    def save(self, tasks: List[Task]) -> None:
        pass

class TextFileStorage(IFileStorage):
    """
    Guarda las tareas en un archivo de texto.
    """
    def save(self, tasks: List[Task]) -> None:
        with open(self.filename, "w") as f:
            for task in tasks:
                f.write(f"{task.id} - {task.name} - {task.user} - {task.completed}\n")

class CSVFileStorage(IFileStorage):
    """
    Guarda las tareas en un archivo CSV.
    """
    def save(self, tasks: List[Task]) -> None:
        with open(self.filename, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "user", "completed"])
            for task in tasks:
                writer.writerow([task.id, task.name, task.user, task.completed])
