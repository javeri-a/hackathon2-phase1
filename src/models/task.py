from dataclasses import dataclass
from typing import Optional
from uuid import uuid4


@dataclass
class Task:
    """
    Represents a todo task with a unique ID, title, description, and completion status.
    
    Attributes:
        id (str): Unique identifier for the task (UUID string representation)
        title (str): Required title of the task (non-empty)
        description (str): Optional detailed description of the task
        completed (bool): Status of whether the task is completed or not
    """
    
    id: str
    title: str
    description: Optional[str] = None
    completed: bool = False
    
    def __post_init__(self):
        """
        Validates the task after initialization.
        Ensures that the title is not empty.
        """
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty")
    
    @classmethod
    def create_task(cls, title: str, description: Optional[str] = None) -> 'Task':
        """
        Creates a new Task instance with a generated UUID.
        
        Args:
            title (str): Required title of the task (non-empty)
            description (str, optional): Optional detailed description of the task
            
        Returns:
            Task: A new Task instance with a unique ID and incomplete status by default
        """
        return cls(
            id=str(uuid4()),
            title=title.strip(),
            description=description,
            completed=False
        )