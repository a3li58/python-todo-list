# Import EasyGUI for graphical user interface (buttons, input boxes, message boxes)
import easygui

# Import JSON to save and load tasks from a file
import json


# Try to load saved tasks from tasks.json when program starts
# If the file does not exist yet, start with an empty task list
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []


# Function to save current tasks into tasks.json
# This keeps tasks saved even after closing the program
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


# Main loop keeps program running until user exits
while True:

    # Show main menu using buttons
    choice = easygui.buttonbox(
        "Choose an option",
        "To Do List",
        ["Add Task", "View Tasks", "Complete Task", "Delete Task", "Exit"]
    )

    # Add a new task
    if choice == "Add Task":

        # Ask user to enter task name
        task_name = easygui.enterbox("Enter task name:")

        # Continue only if user entered something
        if task_name:

            # Ask user to enter task time
            task_time = easygui.enterbox("Enter task time:")

            # Add task to list as dictionary
            # Store task name, time, and completion status
            tasks.append({
                "task": task_name,
                "time": task_time,
                "done": False
            })

            # Save updated task list to file
            save_tasks()

            # Show success message
            easygui.msgbox("Task added successfully!")

    # View all tasks
    elif choice == "View Tasks":

        # Check if task list is empty
        if len(tasks) == 0:
            easygui.msgbox("No tasks found.")
        else:
            task_text = ""

            # Loop through all tasks and display them
            for i, task in enumerate(tasks, start=1):

                # Show check mark if done, cross if not done
                status = "✓" if task["done"] else "✗"

                # Add task details to display text
                task_text += f"{i}. {task['task']} | {task['time']} | {status}\n"

            # Display all tasks in textbox
            easygui.textbox("Your Tasks", "Tasks", task_text)

    # Mark task as completed
    elif choice == "Complete Task":

        # Check if there are tasks available
        if len(tasks) == 0:
            easygui.msgbox("No tasks available.")
        else:
            task_text = ""

            # Display current tasks
            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["done"] else "✗"
                task_text += f"{i}. {task['task']} | {task['time']} | {status}\n"

            # Ask user which task to complete
            task_num = easygui.enterbox(
                "Tasks:\n\n" + task_text + "\nEnter task number to complete:"
            )

            # Check if input is a valid number
            if task_num and task_num.isdigit():
                task_num = int(task_num)

                # Check if number exists in task list
                if 1 <= task_num <= len(tasks):

                    # Change task status to completed
                    tasks[task_num - 1]["done"] = True

                    # Save changes
                    save_tasks()

                    easygui.msgbox("Task completed!")
                else:
                    easygui.msgbox("Invalid task number.")
            else:
                easygui.msgbox("Please enter a valid number.")

    # Delete a task
    elif choice == "Delete Task":

        # Check if task list is empty
        if len(tasks) == 0:
            easygui.msgbox("No tasks to delete.")
        else:
            task_text = ""

            # Display all tasks
            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["done"] else "✗"
                task_text += f"{i}. {task['task']} | {task['time']} | {status}\n"

            # Ask user which task to delete
            task_num = easygui.enterbox(
                "Tasks:\n\n" + task_text + "\nEnter task number to delete:"
            )

            # Check if input is valid
            if task_num and task_num.isdigit():
                task_num = int(task_num)

                # Check if task number exists
                if 1 <= task_num <= len(tasks):

                    # Remove selected task from list
                    deleted_task = tasks.pop(task_num - 1)

                    # Save updated list
                    save_tasks()

                    easygui.msgbox(f"{deleted_task['task']} deleted.")
                else:
                    easygui.msgbox("Invalid task number.")
            else:
                easygui.msgbox("Please enter a valid number.")

    # Exit program
    else:
        easygui.msgbox("Goodbye!")
        break