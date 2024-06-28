# task.py

class Task:
    def __init__(self, title, description, due_date, priority, assigned_to=None, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.assigned_to = assigned_to
        self.completed = completed

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority,
            'assigned_to': self.assigned_to,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, task_dict):
        return cls(
            task_dict['title'],
            task_dict['description'],
            task_dict['due_date'],
            task_dict['priority'],
            task_dict.get('assigned_to'),
            task_dict.get('completed', False)
        )
