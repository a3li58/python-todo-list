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


