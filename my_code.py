tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):     # Enumerate to number tasks
            print(f"{i}. {task}")
# Function to add task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")
# Function to remove a task
def remove_task():
    show_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to remove: "))    
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)    # Remove task by index
                print(f"Task '{removed}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")    # Get user choice
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
//first commit
