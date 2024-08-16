from task_manager import TaskManager
from task import Task


# Create a task manager instance and load tasks from a JSON file
manager = TaskManager()


# Add tasks to the task manager
task1 = Task('Buy groceries', 'Milk, eggs, bread')
task2 = Task('Clean the house', 'Wash the dishes, vacuum, dust')
task3 = Task('Prepare dinner', 'Cook meat, vegetables, and drink')

manager.add_task(task1)
manager.add_task(task2)
manager.add_task(task3)

# List all tasks
print(manager.list_tasks())
