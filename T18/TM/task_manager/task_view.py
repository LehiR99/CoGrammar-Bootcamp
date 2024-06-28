class TaskView:
    @staticmethod
    def display_tasks(tasks):
        if not tasks:
            print("No tasks available.")
        else:
            for task in tasks:
                TaskView.display_task(task)

    @staticmethod
    def display_task(task):
        print(f"Title: {task.title}")
        print(f"Description: {task.description}")
        print(f"Due Date: {task.due_date}")
        print(f"Priority: {task.priority}")
        print(f"Assigned To: {task.assigned_to}")
        print(f"Completed: {'Yes' if task.completed else 'No'}")
        print("-" * 20)
