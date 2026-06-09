
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
