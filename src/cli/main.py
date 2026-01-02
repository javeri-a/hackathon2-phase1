"""
Interactive CLI for the Todo application.
Provides a menu-based interface for managing todo tasks.
"""
from ..services.todo_service import TodoService
from ..models.task import Task
from typing import Optional
import sys


def print_menu():
    """Display the main menu options."""
    print("\n" + "="*40)
    print("TODO APPLICATION - Interactive Menu")
    print("="*40)
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Update a task")
    print("4. Mark task as complete")
    print("5. Mark task as incomplete")
    print("6. Delete a task")
    print("7. Exit")
    print("-"*40)


def get_user_choice() -> int:
    """Get and validate user's menu choice."""
    while True:
        try:
            choice = int(input("Enter your choice (1-7): "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_task_details() -> tuple[str, Optional[str]]:
    """Get task title and description from user."""
    title = input("Enter task title: ").strip()
    if not title:
        raise ValueError("Task title cannot be empty")
    
    description_input = input("Enter task description (optional, press Enter to skip): ").strip()
    description = description_input if description_input else None
    
    return title, description


def get_task_id() -> str:
    """Get task ID from user."""
    task_id = input("Enter task ID: ").strip()
    if not task_id:
        raise ValueError("Task ID cannot be empty")
    return task_id


def display_tasks(tasks):
    """Display all tasks with formatting."""
    if not tasks:
        print("\nNo tasks found.")
        return
    
    print("\nAll Tasks:")
    print("-" * 50)
    for task in tasks:
        status = "X" if task.completed else "O"
        print(f"[{status}] ID: {task.id}")
        print(f"    Title: {task.title}")
        if task.description:
            print(f"    Description: {task.description}")
        print()


def print_success(message: str):
    """Print success message in green (if terminal supports it)."""
    print(f"\033[92m{message}\033[0m")  # Green text


def print_error(message: str):
    """Print error message in red (if terminal supports it)."""
    print(f"\033[91m{message}\033[0m")  # Red text


def handle_add_task(service: TodoService):
    """Handle adding a new task."""
    try:
        title, description = get_task_details()
        task = service.add_task(title, description)
        print_success(f"Task '{task.title}' added successfully!")
        print(f"Task ID: {task.id}")
    except ValueError as e:
        print_error(f"Error: {e}")
    except Exception as e:
        print_error(f"Unexpected error: {e}")


def handle_list_tasks(service: TodoService):
    """Handle listing all tasks."""
    try:
        tasks = service.get_all_tasks()
        display_tasks(tasks)
    except Exception as e:
        print_error(f"Error listing tasks: {e}")


def handle_update_task(service: TodoService):
    """Handle updating an existing task."""
    try:
        task_id = get_task_id()
        task = service.get_task_by_id(task_id)
        if not task:
            print_error(f"Task with ID {task_id} not found.")
            return
        
        print(f"Current task: {task.title}")
        if task.description:
            print(f"Current description: {task.description}")
        
        title_input = input("Enter new title (or press Enter to keep current): ").strip()
        description_input = input("Enter new description (or press Enter to keep current): ").strip()
        
        # Use current values if no new input provided
        new_title = title_input if title_input else task.title
        new_description = description_input if description_input else task.description
        
        # If no changes were made, just return
        if new_title == task.title and new_description == task.description:
            print("No changes made to the task.")
            return
            
        updated_task = service.update_task(task_id, new_title, new_description)
        if updated_task:
            print_success("Task updated successfully!")
            print(f"New title: {updated_task.title}")
            if updated_task.description:
                print(f"New description: {updated_task.description}")
    except ValueError as e:
        print_error(f"Error: {e}")
    except Exception as e:
        print_error(f"Unexpected error: {e}")


def handle_complete_task(service: TodoService):
    """Handle marking a task as complete."""
    try:
        task_id = get_task_id()
        success = service.mark_task_complete(task_id)
        if success:
            print_success("Task marked as complete!")
            task = service.get_task_by_id(task_id)
            if task:
                print(f"Task: {task.title}")
        else:
            print_error(f"Task with ID {task_id} not found.")
    except Exception as e:
        print_error(f"Error marking task as complete: {e}")


def handle_incomplete_task(service: TodoService):
    """Handle marking a task as incomplete."""
    try:
        task_id = get_task_id()
        success = service.mark_task_incomplete(task_id)
        if success:
            print_success("Task marked as incomplete!")
            task = service.get_task_by_id(task_id)
            if task:
                print(f"Task: {task.title}")
        else:
            print_error(f"Task with ID {task_id} not found.")
    except Exception as e:
        print_error(f"Error marking task as incomplete: {e}")


def handle_delete_task(service: TodoService):
    """Handle deleting a task."""
    try:
        task_id = get_task_id()
        success = service.delete_task(task_id)
        if success:
            print_success("Task deleted successfully!")
        else:
            print_error(f"Task with ID {task_id} not found.")
    except Exception as e:
        print_error(f"Error deleting task: {e}")


def main():
    """Main entry point for the interactive CLI."""
    print("Welcome to the Interactive Todo Application!")
    
    service = TodoService()
    
    while True:
        print_menu()
        choice = get_user_choice()
        
        if choice == 1:
            handle_add_task(service)
        elif choice == 2:
            handle_list_tasks(service)
        elif choice == 3:
            handle_update_task(service)
        elif choice == 4:
            handle_complete_task(service)
        elif choice == 5:
            handle_incomplete_task(service)
        elif choice == 6:
            handle_delete_task(service)
        elif choice == 7:
            print("\nThank you for using the Todo Application. Goodbye!")
            sys.exit(0)
        
        # Pause to let user see the result before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()