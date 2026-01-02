import sys
from io import StringIO
from unittest.mock import patch
from src.cli.main import main, create_parser
from src.services.todo_service import TodoService


def test_add_command_integration():
    """Integration test for the add command."""
    service = TodoService()
    
    # Patch the service to simulate the actual app behavior
    with patch('src.cli.main.TodoService') as mock_service_class:
        mock_service = mock_service_class.return_value
        mock_service.add_task.return_value = type('Task', (), {
            'id': 'mock-id',
            'title': 'Test title',
            'description': 'Test description',
            'completed': False
        })()
        
        # Simulate command line arguments
        sys.argv = ['main.py', 'add', '-t', 'Test title', '-d', 'Test description']
        
        # Capture stdout
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            main()
        
        output = captured_output.getvalue()
        assert "Task added successfully!" in output
        assert "Test title" in output


def test_list_command_integration():
    """Integration test for the list command."""
    service = TodoService()
    task = service.add_task("Test task")
    
    with patch('src.cli.main.TodoService') as mock_service_class:
        mock_service = mock_service_class.return_value
        mock_service.get_all_tasks.return_value = [type('Task', (), {
            'id': task.id,
            'title': 'Test task',
            'description': None,
            'completed': False
        })()]
        
        # Simulate command line arguments
        sys.argv = ['main.py', 'list']
        
        # Capture stdout
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            main()
        
        output = captured_output.getvalue()
        assert "All Tasks" in output
        assert "Test task" in output


def test_complete_command_integration():
    """Integration test for the complete command."""
    service = TodoService()
    task = service.add_task("Test task")
    
    with patch('src.cli.main.TodoService') as mock_service_class:
        mock_service = mock_service_class.return_value
        # Mock the get_task_by_id method to return a completed task
        mock_service.mark_task_complete.return_value = True
        mock_service.get_task_by_id.return_value = type('Task', (), {
            'id': task.id,
            'title': 'Test task',
            'description': None,
            'completed': True
        })()
        
        # Simulate command line arguments
        sys.argv = ['main.py', 'complete', '-i', task.id]
        
        # Capture stdout
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            main()
        
        output = captured_output.getvalue()
        assert f"Task {task.id} marked as complete" in output


def test_parser_creation():
    """Test that the argument parser is created correctly."""
    parser = create_parser()
    
    # Test that the parser has the expected subcommands
    assert 'add' in parser._subparsers._group_actions[0].choices
    assert 'list' in parser._subparsers._group_actions[0].choices
    assert 'update' in parser._subparsers._group_actions[0].choices
    assert 'complete' in parser._subparsers._group_actions[0].choices
    assert 'incomplete' in parser._subparsers._group_actions[0].choices
    assert 'delete' in parser._subparsers._group_actions[0].choices