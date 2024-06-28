import json
import os
from models.task import Task


class TaskController:
    """
    A controller to manage tasks.
    """

    def __init__(self, filepath):
        """
        Initialize the TaskController with the path to the JSON file where tasks are stored.

        :param filepath: Path to the JSON file for storing tasks.
        """
        self.filepath = filepath
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """
        Load tasks from the JSON file. If the file doesn't exist, return an empty list.

        :return: List of Task objects.
        """
        try:
            with open(self.filepath, 'r') as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        """
        Save the current list of tasks to the JSON file.
        """
        with open(self.filepath, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file, indent=4)

    def create_task(self, title, description, due_date, priority):
        """
        Create a new task and add it to the list, then save the updated list to the file.

        :param title: Title of the task.
        :param description: Description of the task.
        :param due_date: Due date for the task.
        :param priority: Priority level of the task.
        :return: The newly created Task object.
        """
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()
        return task

    def get_tasks(self):
        """
        Get the current list of tasks.

        :return: List of Task objects.
        """
        return self.tasks

    def delete_task(self, task_title):
        """
        Delete a task by its title and save the updated list to the file.

        :param task_title: Title of the task to be deleted.
        """
        self.tasks = [task for task in self.tasks if task.title != task_title]
        self.save_tasks()
