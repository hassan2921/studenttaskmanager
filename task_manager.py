import json
import os

DATA_FILE = "tasks.json"


class TaskManager:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.tasks = []
        self.load()

    def add_task(self, title):
        task = {"id": self._next_id(), "title": title, "done": False}
        self.tasks.append(task)
        self.save()
        return task

    def _next_id(self):
        return max((t["id"] for t in self.tasks), default=0) + 1

    def list_tasks(self):
        return list(self.tasks)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                self.save()
                return task

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                self.tasks = json.load(f)

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        self.save()

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=2)


def read_id(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        raise ValueError("Task ID must be a number.")


def display(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
    for t in tasks:
        mark = "x" if t["done"] else " "
        print(f"[{mark}] {t['id']}. {t['title']}")
