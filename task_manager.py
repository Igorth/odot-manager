import json
from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.existing_titles = set()

    def add_task(self, task):
        print(f"Adding task: {task.title}")
        if task.title in self.existing_titles:
            raise ValueError(f"Task with title '{task.title}' already exists.")
        self.tasks[task.title] = task
        self.existing_titles.add(task.title)
