class TaskView:
    @staticmethod
    def display_task(task):
        """
        Display the details of a single task.

        :param task: The Task object whose details are to be displayed.
        """
        print(f"Title: {task.title}")
        print(f"Description: {task.description}")
        print(f"Due Date: {task.due_date}")
        print(f"Priority: {task.priority}")
        print(f"Completed: {'Yes' if task.completed else 'No'}")
        print(f"Assigned to: {task.assigned_to}")
        print()

    @staticmethod
    def display_tasks(tasks):
        """
        Display the details of multiple tasks.

        :param tasks: List of Task objects whose details are to be displayed.
        """
        for task in tasks:
            TaskView.display_task(task)
