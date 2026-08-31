"""
Task 1: To-Do List Application
Features:
- Object-oriented design using a Task class.
- Add tasks, view tasks with completion status, mark tasks as complete, and delete tasks.
- Interactive, clean command-line interface.
"""

class Task:
    def __init__(self, task_id: int, description: str):
        self.id = task_id
        self.description = description
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "[✓] Done" if self.is_completed else "[ ] Pending"
        return f"{self.id}. {status} - {self.description}"


class ToDoListApp:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, description: str):
        cleaned_desc = description.strip()
        if not cleaned_desc:
            print("\nError: Task description cannot be empty.")
            return
        
        new_task = Task(self._next_id, cleaned_desc)
        self.tasks.append(new_task)
        self._next_id += 1
        print(f"\nTask added successfully! (ID: {new_task.id})")

    def view_tasks(self):
        if not self.tasks:
            print("\nYour to-do list is empty.")
            return

        print("\n--- Current To-Do List ---")
        for task in self.tasks:
            print(task)
        print("--------------------------")

    def mark_task_completed(self, task_id: int):
        task = self._find_task(task_id)
        if task:
            if task.is_completed:
                print(f"\nTask {task_id} is already marked as completed.")
            else:
                task.mark_completed()
                print(f"\nTask {task_id} marked as completed!")
        else:
            print(f"\nError: Task with ID {task_id} not found.")

    def delete_task(self, task_id: int):
        task = self._find_task(task_id)
        if task:
            self.tasks.remove(task)
            print(f"\nTask {task_id} deleted successfully.")
        else:
            print(f"\nError: Task with ID {task_id} not found.")

    def _find_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def run(self):
        while True:
            print("\n==============================")
            print("     TO-DO LIST MANAGER       ")
            print("==============================")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == "1":
                self.view_tasks()
            elif choice == "2":
                desc = input("Enter task description: ")
                self.add_task(desc)
            elif choice == "3":
                self.view_tasks()
                if self.tasks:
                    try:
                        task_id = int(input("\nEnter task ID to mark as done: "))
                        self.mark_task_completed(task_id)
                    except ValueError:
                        print("\nError: Please enter a valid numeric Task ID.")
            elif choice == "4":
                self.view_tasks()
                if self.tasks:
                    try:
                        task_id = int(input("\nEnter task ID to delete: "))
                        self.delete_task(task_id)
                    except ValueError:
                        print("\nError: Please enter a valid numeric Task ID.")
            elif choice == "5":
                print("\nExiting To-Do List Manager. Have a productive day!")
                break
            else:
                print("\nInvalid option. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    app = ToDoListApp()
    app.run()
    