import unittest
from task_manager import TaskManager
from task import Task


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = Task("Study for exam", "Prepare for the upcoming exam")
        self.manager.add_task(task)
        self.assertIn("Study for exam", self.manager.tasks)

    def test_add_duplicate_task(self):
        task = Task("Study for exam", "Prepare for the upcoming exam")
        self.manager.add_task(task)
        with self.assertRaises(ValueError):
            self.manager.add_task(task)


if __name__ == "__main__":
    unittest.main()
