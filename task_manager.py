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

    def save_to_json(self, path='tasks.json'):
        with open(path, 'w') as file:
            json.dump(self.list_tasks(), file)

    def load_from_json(self, path='tasks.json'):
        try:
            with open(path, 'r') as file:
                tasks = json.load(file)
                for task_data in tasks:
                    task = Task.from_dict(task_data)
                    self.add_task(task)
        except FileNotFoundError:
            print(f"File '{path}' not found. Creating an empty task list.")
