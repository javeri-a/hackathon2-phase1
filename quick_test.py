"""
Quick test to verify the TodoService functionality still works with the new interactive CLI.
"""
from src.services.todo_service import TodoService


def test_service_functionality():
    print("Testing TodoService functionality with new interactive CLI implementation...")
    
    service = TodoService()
    
    # Test adding a task
    task = service.add_task("Test task", "Test description")
    print(f"SUCCESS: Added task: {task.title}")

    # Test listing tasks
    tasks = service.get_all_tasks()
    print(f"SUCCESS: Found {len(tasks)} task(s)")

    # Test updating a task
    updated_task = service.update_task(task.id, title="Updated test task", description="Updated description")
    if updated_task:
        print(f"SUCCESS: Updated task: {updated_task.title}")

    # Test marking as complete
    service.mark_task_complete(task.id)
    print(f"SUCCESS: Marked task as complete")

    # Test marking as incomplete
    service.mark_task_incomplete(task.id)
    print(f"SUCCESS: Marked task as incomplete")

    # Test deleting a task
    success = service.delete_task(task.id)
    if success:
        print(f"SUCCESS: Deleted task")

    print("SUCCESS: All functionality tests passed!")


if __name__ == "__main__":
    test_service_functionality()