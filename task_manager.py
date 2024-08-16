import json
from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.existing_titles = set()

    def add_task(self, task):
        if task.title in self.existing_titles:
            raise ValueError(f"Task with title '{task.title}' already exists.")
        self.tasks[task.title] = task
        self.existing_titles.add(task.title)

    def list_tasks(self):
        return [task.to_dict() for task in self.tasks.values()]

    def delete_task(self, title):
        if title in self.tasks:
            del self.tasks[title]
            self.existing_titles.remove(title)
        else:
            raise KeyError(f"Task with title '{title}' not found.")
