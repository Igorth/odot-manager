import unittest
from task import Task


class TestTask(unittest.TestCase):

    def test_create_task(self):
        task = Task("Finish report", "Write up the results of the project")
        self.assertEqual(task.title, "Finish report")
        self.assertEqual(task.completed, False)

    def test_mark_as_completed(self):
        task = Task("Finish report", "Write up the results of the project")
        task.mark_as_completed()
        self.assertEqual(task.completed, True)


if __name__ == '__main__':
    unittest.main()
