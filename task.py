class Task:
    def __init__(self, id: int, name: str, user: str) -> None:
        self.id: int = id
        self.name: str = name
        self.user: str = user
        self.completed: bool = False

    def complete(self) -> None:
        self.completed = True
