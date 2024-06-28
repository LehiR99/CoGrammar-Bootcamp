import unittest
import os
from ..controllers.task_controller import TaskController
# from T18.task_manager.controllers.task_controller import TaskController

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # Use a separate file for testing to avoid conflicts with production data
        self.test_file_path = 'test_tasks.json'
        self.controller = TaskController(self.test_file_path)
        self.controller.tasks = []  # Ensure starting with an empty list

    def tearDown(self):
        # Clean up the test file after tests
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_create_task(self):
        task = self.controller.create_task("Test Task", "Test Description", "2024-06-30", 1)
        self.assertEqual(len(self.controller.tasks), 1)
        self.assertEqual(task.title, "Test Task")

    def test_mark_task_complete(self):
        task = self.controller.create_task("Test Task", "Test Description", "2024-06-30", 1)
        task.mark_as_complete()
        self.assertTrue(task.completed)

    def test_delete_task(self):
        self.controller.create_task("Test Task 1", "Test Description", "2024-06-30", 1)
        self.controller.create_task("Test Task 2", "Test Description", "2024-07-15", 2)
        self.controller.delete_task("Test Task 1")
        self.assertEqual(len(self.controller.tasks), 1)
        self.assertEqual(self.controller.tasks[0].title, "Test Task 2")

    def test_assign_task(self):
        task = self.controller.create_task("Test Task", "Test Description", "2024-06-30", 1)
        task.assign_to("User 1")
        self.assertEqual(task.assigned_to, "User 1")

    def test_set_due_date(self):
        task = self.controller.create_task("Test Task", "Test Description", "2024-06-30", 1)
        task.update_details(due_date="2024-07-01")
        self.assertEqual(task.due_date, "2024-07-01")


if __name__ == '__main__':
    unittest.main()
