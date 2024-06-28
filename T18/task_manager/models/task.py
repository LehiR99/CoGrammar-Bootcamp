class Task:
    def __init__(self, title, description, due_date, priority, completed=False, assigned_to=None):

    # Initializes a new task with the given details.


        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed
        self.assigned_to = assigned_to

    def mark_as_complete(self):

        # Marks the task as completed.

        self.completed = True

    def update_details(self, title=None, description=None, due_date=None, priority=None):

        #Updates the task details.

        if title:
            self.title = title
        if description:
            self.description = description
        if due_date:
            self.due_date = due_date
        if priority:
            self.priority = priority

