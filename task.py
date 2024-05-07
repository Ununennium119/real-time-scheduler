class Task:
    def __init__(self, id: int, arrival_time: int, execution_time: int, deadline: int):
        self.id: int = id
        self.arrival_time: int = arrival_time
        self.execution_time: int = execution_time
        self.deadline: int = deadline
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Task):
            return False
        return value.id == self.id
    
    def __repr__(self) -> str:
        return f'Task(id={self.id})'
    
    def __str__(self) -> str:
        return self.__repr__()
