def delete_task(tasks):
    if not tasks:
        print("No tasks to delete!")
        return

    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    try:
        task_num = int(input("\nEnter the task number to delete: "))

        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'"{removed_task}" has been deleted.')
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")