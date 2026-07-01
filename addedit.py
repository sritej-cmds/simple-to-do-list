

def add_task(task):
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

def edit_task(task):
    task_number = int(input("Enter task number: "))
    new_task = input("Enter new task: ")

    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1] = new_task
        print("Task updated!")
    else:
        print("Invalid task number.")
