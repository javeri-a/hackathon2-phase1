from typing import List, Optional
from ..models.task import Task


class TodoService:
    """
    Service class that handles all business logic for todo operations.
    Manages a collection of tasks in memory.
    """
    
    def __init__(self):
        """Initialize an empty list of tasks."""
        self._tasks: List[Task] = []
    
    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task to the collection.
        
        Args:
            title (str): Required title of the task (non-empty)
            description (str, optional): Optional detailed description of the task
            
        Returns:
            Task: The newly created task with a unique ID and incomplete status
            
        Raises:
            ValueError: If the title is empty
        """
        task = Task.create_task(title, description)
        self._tasks.append(task)
        return task
    
    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks from the collection.
        
        Returns:
            List[Task]: A list of all tasks
        """
        return self._tasks.copy()
    
    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        """
        Retrieve a task by its ID.
        
        Args:
            task_id (str): The ID of the task to retrieve
            
        Returns:
            Task: The task with the specified ID, or None if not found
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(
        self, 
        task_id: str, 
        title: Optional[str] = None, 
        description: Optional[str] = None
    ) -> Optional[Task]:
        """
        Update an existing task's title or description.
        
        Args:
            task_id (str): The ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task
            
        Returns:
            Task: The updated task, or None if the task with the given ID was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return None
        
        if title is not None:
            title = title.strip()
            if not title:
                raise ValueError("Task title cannot be empty")
            task.title = title
        
        if description is not None:
            task.description = description
            
        return task
    
    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id (str): The ID of the task to delete
            
        Returns:
            bool: True if the task was successfully deleted, False if not found
        """
        task_to_remove = self.get_task_by_id(task_id)
        if task_to_remove:
            self._tasks.remove(task_to_remove)
            return True
        return False
    
    def mark_task_complete(self, task_id: str) -> bool:
        """
        Mark a task as complete by its ID.
        
        Args:
            task_id (str): The ID of the task to mark as complete
            
        Returns:
            bool: True if the task was successfully marked as complete, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
            return True
        return False
    
    def mark_task_incomplete(self, task_id: str) -> bool:
        """
        Mark a task as incomplete by its ID.
        
        Args:
            task_id (str): The ID of the task to mark as incomplete
            
        Returns:
            bool: True if the task was successfully marked as incomplete, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            return True
        return False