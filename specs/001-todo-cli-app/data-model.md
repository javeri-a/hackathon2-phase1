# Data Model: In-Memory Todo Console Application

## Task Entity

**Entity Name**: Task

**Fields**:
- `id`: UUID (string representation) - Unique identifier for the task
- `title`: String - Required title of the task (non-empty)
- `description`: String (optional) - Optional detailed description of the task
- `completed`: Boolean - Status of whether the task is completed or not

**Relationships**: None (standalone entity)

**Validation Rules**:
- `id`: Must be a valid UUID string
- `title`: Must be non-empty string (length > 0)
- `description`: Can be empty or null
- `completed`: Must be a boolean value (default: False)

**State Transitions**:
- `incomplete` → `complete`: When task is marked as done
- `complete` → `incomplete`: When task completion status is reverted

## TaskCollection Entity

**Entity Name**: TaskCollection

**Fields**:
- `tasks`: List of Task entities - Collection of all tasks

**Relationships**: Contains multiple Task entities

**Validation Rules**:
- `tasks`: Must be a list of valid Task entities
- `tasks`: Each ID in the collection must be unique

**State Transitions**:
- `tasks` updated: When tasks are added, updated, or removed