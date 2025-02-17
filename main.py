from task_manager import TaskManager
from task_storage import TextFileStorage

# Ejemplo de uso

# ================================================
# Paso 1. Gestionamos las tareas
# ================================================
tm = TaskManager()
tm.add_task("Aprender SOLID", "Juan")
tm.add_task("Escribir documentación", "María")
tm.add_task("Revisar código", "Pedro")
tm.add_task("Implementar pruebas", "Ana")
tm.complete_task(1)
tm.complete_task(2)

# ================================================
# Paso 2. Proceso de guardado.
# ================================================
# Guardamos en archivo de texto
storage = TextFileStorage("tasks.txt")
tm.save(storage)