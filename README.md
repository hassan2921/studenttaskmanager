# Student Task Manager

A small Python console app to manage study tasks.

Project status: Under Review

## Features
- Add tasks (empty titles are rejected)
- Display all tasks with completion status
- Mark tasks as completed
- Delete tasks by ID
- Tasks saved to `tasks.json`

## Setup
```bash
git clone https://github.com/hassan2921/studenttaskmanager.git
cd studenttaskmanager
python --version   # Python 3.8+ required, no extra packages
```

## Usage
```bash
python task_manager.py
```
Choose 1 (Add), 2 (Show), 3 (Complete), 4 (Delete), or 5 (Quit).

## Running Tests
```bash
python -m unittest discover -s tests -v
```

## License
MIT
