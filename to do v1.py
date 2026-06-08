

tasks = []

while True:
    print("\n TO DO LIST ")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")