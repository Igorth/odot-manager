class Task:
    def __init__(self, title, description=""):
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def edit(self, new_title=None, new_description=None):
        if new_title:
            self.title = new_title
        if new_description:
            self.description = new_description

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"], data["description"])
        if data["completed"]:
            task.mark_as_completed()
        return task
