import os
from task_controller import TaskController
from task_view import TaskView


def main():
    file_path = 'data/tasks.json'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    controller = TaskController(file_path)

    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Delete Task")
        print("3. Update Task")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = int(input("Enter priority (1-5): "))
            assigned_to = input("Enter assigned to: ")
            controller.create_task(title, description, due_date, priority, assigned_to)
            print("Task created successfully.")

        elif choice == '2':
            title = input("Enter the title of the task to delete: ")
            controller.delete_task(title)
            print("Task deleted successfully.")

        elif choice == '3':
            title = input("Enter the title of the task to update: ")
            print("Leave fields blank to skip updating them.")
            new_title = input("Enter new title: ")
            description = input("Enter new description: ")
            due_date = input("Enter new due date (YYYY-MM-DD): ")
            priority = input("Enter new priority (1-5): ")
            assigned_to = input("Enter new assigned to: ")
            completed = input("Is the task completed? (yes/no): ").lower() == 'yes'

            if priority:
                priority = int(priority)

            success = controller.update_task(title, new_title, description, due_date, priority, assigned_to, completed)
            if success:
                print("Task updated successfully.")
            else:
                print("Task not found.")

        elif choice == '4':
            tasks = controller.get_tasks()
            TaskView.display_tasks(tasks)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
