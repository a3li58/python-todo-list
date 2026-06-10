
tasks = []

while True:
    print("\n To Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    
    if choice == "1":
        task_name = input("Enter a task: ")

        tasks.append({
            "task": task_name,
            "done": False
        })

        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["done"] else "✗"
                print(f"{i}. {task['task']} {status}")

    # Complete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["done"] else "✗"
                print(f"{i}. {task['task']} {status}")

            task_num = int(input("Enter task number to complete: "))

            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["done"] = True
                print("Task completed!")
            else:
                print("Invalid task number.")
    # Delete Task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["done"] else "✗"
                print(f"{i}. {task['task']} {status}")

            task_num = int(input("Enter task number to delete: "))

            if 1 <= task_num <= len(tasks):
                deleted_task = tasks.pop(task_num - 1)
                print(f"{deleted_task['task']} deleted.")
            else:
                print("Invalid task number.")



