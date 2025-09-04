"""To-Do List program to add, show, and remove tasks."""
tasks = []
def show_tasks():
    """Displays all tasks in the list."""
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
def add_task():
    """Adds a new task to the list."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")
def remove_task():
    """Removes a task by its number."""
    show_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to remove: ")) 
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Task '{removed}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
def main():
    """Runs the main menu loop for the To-Do List."""
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
if __name__ == "__main__":
    main()
