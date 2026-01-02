import pytest
from src.models.task import Task


def test_create_task_with_valid_data():
    """Test creating a task with valid title and description."""
    task = Task.create_task("Test title", "Test description")
    
    assert task.title == "Test title"
    assert task.description == "Test description"
    assert task.completed is False
    assert task.id is not None
    assert len(task.id) > 0


def test_create_task_without_description():
    """Test creating a task with only a title."""
    task = Task.create_task("Test title")
    
    assert task.title == "Test title"
    assert task.description is None
    assert task.completed is False
    assert task.id is not None


def test_create_task_empty_title():
    """Test creating a task with an empty title raises ValueError."""
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        Task.create_task("")


def test_create_task_whitespace_only_title():
    """Test creating a task with whitespace-only title raises ValueError."""
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        Task.create_task("   ")


def test_create_task_title_with_leading_trailing_spaces():
    """Test that title is automatically stripped of leading/trailing spaces."""
    task = Task.create_task("  Test title  ")
    
    assert task.title == "Test title"


def test_task_initial_completion_status():
    """Test that new tasks are created with completed=False by default."""
    task = Task.create_task("Test title")
    
    assert task.completed is False


def test_direct_task_initialization():
    """Test creating a Task directly with all parameters."""
    task_id = "12345"
    task = Task(id=task_id, title="Test title", description="Test description", completed=True)
    
    assert task.id == task_id
    assert task.title == "Test title"
    assert task.description == "Test description"
    assert task.completed is True


def test_direct_task_initialization_empty_title():
    """Test that direct Task initialization with empty title raises ValueError."""
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        Task(id="12345", title="", description="Test description", completed=False)