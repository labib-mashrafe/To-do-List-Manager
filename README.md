# To-Do List Manager

A command-line task manager in Python. Add tasks, mark them as done, and view their status. Tasks are saved to a JSON file, so they persist between sessions.

## Features

- Add tasks, with validation that rejects empty or numbers-only names
- Mark tasks as done by number, with input validation
- View all tasks with their status (Pending / Done)
- Saves all tasks to `tasks.json` automatically

## How to Run

Requires Python 3.

```
python todo_list_manager.py
```

Tasks are stored in `tasks.json` in the same folder. The file is created automatically on first use.

## Example

```
1. Add task
2. Mark task done
3. View tasks
4. Exit
Enter choice: 1
Enter task name: 123
Task name cannot be just numbers!

Enter choice: 1
Enter task name: Watch F1 Qualifying
Task 'Watch F1 Qualifying' added!

Enter choice: 2
1. Watch F1 Qualifying - Pending
Enter task number to mark done: 1
Task 'Watch F1 Qualifying' marked as done!
```

## What I Learned

- Validating input with `try/except` and string methods like `.isdigit()`
- Saving and loading data with JSON
- Structuring a program with a `main()` function

## License

MIT
