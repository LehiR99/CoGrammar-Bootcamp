import json
import os
from task import Task


class TaskController:
    def __init__(self, filepath):
        self.filepath = filepath
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filepath) and os.path.getsize(self.filepath) > 0:
            with open(self.filepath, 'r') as file:
                try:
                    tasks_data = json.load(file)
                    return [Task.from_dict(task) for task in tasks_data]
                except json.JSONDecodeError:
                    return []
        return []

    def save_tasks(self):
        with open(self.filepath, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def create_task(self, title, description, due_date, priority, assigned_to=None):
        task = Task(title, description, due_date, priority, assigned_to)
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]
        self.save_tasks()

    def update_task(self, title, new_title=None, description=None, due_date=None, priority=None, assigned_to=None, completed=None):
        for task in self.tasks:
            if task.title == title:
                if new_title:
                    task.title = new_title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if priority is not None:
                    task.priority = priority
                if assigned_to:
                    task.assigned_to = assigned_to
                if completed is not None:
                    task.completed = completed
                self.save_tasks()
                return True
        return False

    def get_tasks(self):
        return self.tasks
