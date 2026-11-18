import os
import tempfile
import unittest

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        fd, self.path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        os.remove(self.path)
        self.manager = TaskManager(self.path)

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_add_task(self):
        task = self.manager.add_task("Study Git")
        self.assertEqual(task["title"], "Study Git")
        self.assertFalse(task["done"])
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_complete_task(self):
        task = self.manager.add_task("Finish assignment")
        self.manager.complete_task(task["id"])
        self.assertTrue(self.manager.list_tasks()[0]["done"])

    def test_delete_task(self):
        task = self.manager.add_task("Temporary task")
        self.manager.delete_task(task["id"])
        self.assertEqual(self.manager.list_tasks(), [])

    def test_empty_title_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")


if __name__ == "__main__":
    unittest.main()
