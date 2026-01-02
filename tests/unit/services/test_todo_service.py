import pytest
from src.services.todo_service import TodoService
from src.models.task import Task


class TestTodoService:
    """Tests for the TodoService class."""
    
    def setup_method(self):
        """Set up a fresh service instance for each test."""
        self.service = TodoService()
    
    def test_add_task_creates_new_task(self):
        """Test that adding a task creates a new task with correct attributes."""
        task = self.service.add_task("Test title", "Test description")
        
        assert len(self.service.get_all_tasks()) == 1
        assert task.title == "Test title"
        assert task.description == "Test description"
        assert task.completed is False
        assert task.id is not None
    
    def test_add_task_without_description(self):
        """Test adding a task without description."""
        task = self.service.add_task("Test title")
        
        assert task.title == "Test title"
        assert task.description is None
    
    def test_add_task_empty_title_raises_error(self):
        """Test that adding a task with empty title raises ValueError."""
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            self.service.add_task("")
    
    def test_get_all_tasks_empty_initially(self):
        """Test that initially there are no tasks."""
        tasks = self.service.get_all_tasks()
        
        assert len(tasks) == 0
    
    def test_get_all_tasks_returns_all_added_tasks(self):
        """Test that get_all_tasks returns all added tasks."""
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")
        task3 = self.service.add_task("Task 3")
        
        tasks = self.service.get_all_tasks()
        
        assert len(tasks) == 3
        assert task1 in tasks
        assert task2 in tasks
        assert task3 in tasks
    
    def test_get_task_by_id_finds_existing_task(self):
        """Test that get_task_by_id returns the correct task."""
        task = self.service.add_task("Test task")
        found_task = self.service.get_task_by_id(task.id)
        
        assert found_task is not None
        assert found_task.id == task.id
        assert found_task.title == task.title
    
    def test_get_task_by_id_returns_none_for_nonexistent_task(self):
        """Test that get_task_by_id returns None for non-existent task."""
        result = self.service.get_task_by_id("nonexistent-id")
        
        assert result is None
    
    def test_update_task_title(self):
        """Test updating a task's title."""
        task = self.service.add_task("Original title")
        updated_task = self.service.update_task(task.id, title="New title")
        
        assert updated_task is not None
        assert updated_task.title == "New title"
        # Verify the task list is updated
        all_tasks = self.service.get_all_tasks()
        assert len(all_tasks) == 1
        assert all_tasks[0].title == "New title"
    
    def test_update_task_description(self):
        """Test updating a task's description."""
        task = self.service.add_task("Test title", "Original description")
        updated_task = self.service.update_task(task.id, description="New description")
        
        assert updated_task is not None
        assert updated_task.description == "New description"
    
    def test_update_task_both_fields(self):
        """Test updating both title and description."""
        task = self.service.add_task("Original title", "Original description")
        updated_task = self.service.update_task(task.id, title="New title", description="New description")
        
        assert updated_task is not None
        assert updated_task.title == "New title"
        assert updated_task.description == "New description"
    
    def test_update_task_nonexistent_id(self):
        """Test that updating a non-existent task returns None."""
        result = self.service.update_task("nonexistent-id", title="New title")
        
        assert result is None
    
    def test_update_task_empty_title_raises_error(self):
        """Test that updating a task with empty title raises ValueError."""
        task = self.service.add_task("Original title")
        
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            self.service.update_task(task.id, title="")
    
    def test_delete_task_existing(self):
        """Test deleting an existing task."""
        task = self.service.add_task("Test title")
        success = self.service.delete_task(task.id)
        
        assert success is True
        assert len(self.service.get_all_tasks()) == 0
    
    def test_delete_task_nonexistent(self):
        """Test that deleting a non-existent task returns False."""
        success = self.service.delete_task("nonexistent-id")
        
        assert success is False
    
    def test_mark_task_complete(self):
        """Test marking a task as complete."""
        task = self.service.add_task("Test title")
        success = self.service.mark_task_complete(task.id)
        
        assert success is True
        assert task.completed is True
    
    def test_mark_task_incomplete(self):
        """Test marking a task as incomplete."""
        task = self.service.add_task("Test title")
        # First mark as complete
        self.service.mark_task_complete(task.id)
        # Then mark as incomplete
        success = self.service.mark_task_incomplete(task.id)
        
        assert success is True
        assert task.completed is False
    
    def test_mark_task_complete_nonexistent(self):
        """Test that marking a non-existent task as complete returns False."""
        success = self.service.mark_task_complete("nonexistent-id")
        
        assert success is False
    
    def test_mark_task_incomplete_nonexistent(self):
        """Test that marking a non-existent task as incomplete returns False."""
        success = self.service.mark_task_incomplete("nonexistent-id")
        
        assert success is False