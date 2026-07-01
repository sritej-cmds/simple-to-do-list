tasks = [
    "Learn Git",
    "Learn Python",
    "Build To-Do App"
]

def add_task():
    pass

def edit_task():
    pass

def delete_task():
    pass

def view_tasks():
    print("\nTasks:")

    if not tasks:
        print("No tasks available")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def complete_task():
    view_tasks()

    task_num = int(input("\nEnter task number to complete: "))

    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1] += " ✓"
        print("Task completed!")
    else:
        print("Invalid task number")

while True:
    print("\n===== TO DO APP =====")
    print("1. View Tasks")
    print("2. Complete Task")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_tasks()

    elif choice == "2":
        complete_task()

    elif choice == "3":
        break

    else:
        print("Invalid choice")