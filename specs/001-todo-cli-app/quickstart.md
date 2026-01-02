# Quickstart Guide: Todo Console Application

## Prerequisites

- Python 3.13 or higher
- Standard Python libraries (no external dependencies required)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Navigate to the project directory where the application is located.

## Usage

Run the application using Python:

```bash
python -m src.cli.main [command] [options]
```

### Available Commands

#### Add a Task
```bash
python -m src.cli.main add --title "Task title" --description "Optional description"
```
or
```bash
python -m src.cli.main add -t "Task title" -d "Optional description"
```

#### List All Tasks
```bash
python -m src.cli.main list
```
or
```bash
python -m src.cli.main ls
```

#### Update a Task
```bash
python -m src.cli.main update --id <task_id> --title "New title" --description "New description"
```
or
```bash
python -m src.cli.main update -i <task_id> -t "New title" -d "New description"
```

#### Mark Task as Complete
```bash
python -m src.cli.main complete --id <task_id>
```
or
```bash
python -m src.cli.main complete -i <task_id>
```

#### Mark Task as Incomplete
```bash
python -m src.cli.main incomplete --id <task_id>
```
or
```bash
python -m src.cli.main incomplete -i <task_id>
```

#### Delete a Task
```bash
python -m src.cli.main delete --id <task_id>
```
or
```bash
python -m src.cli.main delete -i <task_id>
```

## Examples

1. Add a new task:
   ```bash
   python -m src.cli.main add -t "Buy groceries" -d "Milk, bread, eggs"
   ```

2. List all tasks:
   ```bash
   python -m src.cli.main list
   ```

3. Mark a task as complete (use the ID shown in the list):
   ```bash
   python -m src.cli.main complete -i 550e8400-e29b-41d4-a716-446655440000
   ```

4. Update a task:
   ```bash
   python -m src.cli.main update -i 550e8400-e29b-41d4-a716-446655440000 -d "Milk, bread, eggs, apples"
   ```

## Notes

- All data is stored in memory only and will be lost when the application exits
- Task IDs are automatically generated using UUIDs
- Empty task titles are not allowed
- Use the list command to see all tasks with their IDs before updating, completing, or deleting