from abc import ABC, abstractmethod
import csv
from typing import List
from task import Task

class IStorage(ABC):
    """
    Interfaz para guardar las tareas.
    """
    @abstractmethod
    def save(self, tasks: List[Task]) -> None:
        pass

class IFileStorage(IStorage):
    """
    Guarda las tareas en un archivo.
    """
    def __init__(self, filename: str) -> None:
        self.filename = filename

class IDBStorage(IStorage):
    """
    Guarda las tareas en una base de datos.
    """
    
    @abstractmethod
    def health_check(self) -> bool:
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

class SQLiteDatabaseStorage(IFileStorage):
    """
    Guarda las tareas en una base de datos tipo archivo.
    """
    def save(self, tasks: List[Task]) -> None:
        print(f"Guardando en base de datos {self.filename}...")

class MySQLDatabaseStorage(IDBStorage):
    """
    Guarda las tareas en una base de datos tipo MySQL.
    """
    
    def save(self, tasks: List[Task]) -> None:
        print(f"Guardando en base de datos MYSQL...")
            
    def health_check(self) -> bool:
        """
        Verifica si el motor de la base de datos está funcionando.
        """
        return True
