import json # saving and loading data
import os # checking if the file exists
from datetime import datetime

# creating a list to store the task dictionaries inside it
tasks = []
task_counter = 0
file_name = "tasks.json" 

# loading tasks once the program runs
def load_tasks() :
    global tasks, task_counter
    if os.path.exists(file_name) :
        # opens the file in read mode and when the code is finished it closes it automatically
        with open(file_name, "r") as file :
            tasks = json.load(file)
            if tasks:
                task_counter = max(t['id'] for t in tasks)

# saving the tasks inside the json file
def save_tasks() :
    with open(file_name, "w") as file :
        json.dump(tasks, file, indent=4)

# adding task
def add_task() : 
    global task_counter
    title = input("Enter the task to do : ")
    task_counter += 1
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_task = {
        "id" : task_counter,
        "title" : title,
        "done" : False,
        "created_at" : now 
    }
    
    tasks.append(new_task)
    save_tasks()
    print("Task added successfully !")

# view tasks
def view_tasks() :
    if not tasks :
        print("\nYour to-do list is empty.")
        return
    
    print("\n Your tasks : ")
    for t in tasks : 
        status = "✔ Done" if t["done"] else "✖ Not Done"
        print(f"ID: {t['id']} | {t['title']} | {status} | {t['created_at']}")

# mark task as done
def mark_done() : 
    view_tasks()
    if not tasks : return
    
    try : 
        task_id = int(input("Entre the task ID you want to mark as done : "))
        for t in tasks : 
            if t['id'] == task_id :
                t['done'] = True
                save_tasks()
                print(f"Task {task_id} marked as done!")
                return
        print("Task ID not found !")
    except ValueError :
        print("Invalid input, please enter a numeric ID !")

# delete task
def delete_task() : 
    view_tasks()
    if not tasks : return
    
    try : 
        task_id = int(input("Enter the task ID you want to delete : "))
        for t in tasks :
            if t['id'] == task_id : 
                tasks.remove(t)
                save_tasks()
                print(f"Task {task_id} deleted.")
                return
        print("Task ID not found.")
    except ValueError : 
        print("Invalid input!")
        
# edit task
def edit_task() :
    view_tasks()
    if not tasks : return 
    
    try : 
        task_id = int(input("Enter the task ID you want to edit : "))
        for t in tasks : 
            if t['id'] == task_id :
                new_title = input("Enter the new title of the task : ")
                t['title'] = new_title
                save_tasks()
                print("Task edited successfully!")
                return
        print("Task ID not found.")
    except ValueError : 
        print("Invalid input!")

def main() : 
    load_tasks()
    
    while True : 
        print("\n MENU :",
                "\n 1. Add Task",
                "\n 2. View Tasks",
                "\n 3. Mark Task as Done",
                "\n 4. Delete Task",
                "\n 5. Edit Task",
                "\n 6. Exit")
        
        option = input("Select an option : ")
        
        match option : 
            case '1' : add_task()
            case '2' : view_tasks()
            case '3' : mark_done()
            case '4' : delete_task()
            case '5' : edit_task()
            case '6' :
                print("Exiting the app..")
                return
            case _ :
                print("Invalid menu input. Try again \n")
                
main()