from task import Task


# Create a task and print it
task = Task("Buy groceries", "Milk, eggs, bread")
print(task.to_dict())

# Mark the task as complete
task.mark_as_completed()
print(task.to_dict())
