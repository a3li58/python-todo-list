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

