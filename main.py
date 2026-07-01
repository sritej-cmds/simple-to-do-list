from addedit import add_task, edit_task
from app import delete_task

tasks = [
    "Learn Git",
    "Learn Python",
    "Build To-Do App"
]


def view_tasks(tasks):
    print("\nTasks:")

    if not tasks:
        print("No tasks available")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_num = int(input("\nEnter task number to complete: "))

        if 1 <= task_num <= len(tasks):
            if "✓" not in tasks[task_num - 1]:
                tasks[task_num - 1] += " ✓"
                print("Task completed!")
            else:
                print("Task is already completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n===== TO DO APP =====")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. View Tasks")
    print("5. Complete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        edit_task(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        view_tasks(tasks)

    elif choice == "5":
        complete_task(tasks)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
