import easygui
import json


try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []



def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


while True:
    choice = easygui.buttonbox(
        "Choose an option",
        "To Do List",
        ["Add Task", "View Tasks", "Complete Task", "Delete Task", "Exit"]
    )
    if choice == "Add Task":
        task_name = easygui.enterbox("Enter task name:")
        if task_name:
            task_time = easygui.enterbox("Enter task time:")

            tasks.append({
                "task": task_name,
                "time": task_time,
                "done": False
            })

            save_tasks()
            easygui.msgbox("Task added successfully!")
    elif choice == "View Tasks":
        if len(tasks) == 0:
            easygui.msgbox("No tasks found.")
        else:
            task_text = ""

            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["done"] else "✗"
                task_text += f"{i}. {task['task']} | {task['time']} | {status}\n"

            easygui.textbox("Your Tasks", "Tasks", task_text)

   
    elif choice == "Complete Task":
        if len(tasks) == 0:
            easygui.msgbox("No tasks available.")
        else:
            task_text = ""

            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["done"] else "✗"
                task_text += f"{i}. {task['task']} | {task['time']} | {status}\n"

            task_num = easygui.enterbox(
                "Tasks:\n\n" + task_text + "\nEnter task number to complete:"
            )

            if task_num and task_num.isdigit():
                task_num = int(task_num)

                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["done"] = True
                    save_tasks()
                    easygui.msgbox("Task completed!")
                else:
                    easygui.msgbox("Invalid task number.")
            else:
                easygui.msgbox("Please enter a valid number.")

    
    elif choice == "Delete Task":
        if len(tasks) == 0:
            easygui.msgbox("No tasks to delete.")
        else:
            task_text = ""

            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["done"] else "✗"
                task_text += f"{i}. {task['task']} | {task['time']} | {status}\n"

            task_num = easygui.enterbox(
                "Tasks:\n\n" + task_text + "\nEnter task number to delete:"
            )

            if task_num and task_num.isdigit():
                task_num = int(task_num)

                if 1 <= task_num <= len(tasks):
                    deleted_task = tasks.pop(task_num - 1)
                    save_tasks()
                    easygui.msgbox(f"{deleted_task['task']} deleted.")
                else:
                    easygui.msgbox("Invalid task number.")
            else:
                easygui.msgbox("Please enter a valid number.")
    else:
        easygui.msgbox("Goodbye!")
        break

