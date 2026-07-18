import json
import sys
import os 
filename = "tasks.json"
if not os.path.exists(filename):
    with open(filename, "w") as file:
        json.dump([], file) 
if len(sys.argv) > 1 and sys.argv[1] == "add":
    
    with open(filename, "r") as f:
        tasks = json.load(f) # Now 'tasks' is a Python list
        new_id = len(tasks) + 1
    
    
    new_task = {
        "id": new_id,
        "description": sys.argv[2],
        "status": "todo"
    }   
    tasks.append(new_task)
    
    
    with open(filename, "w") as f:
        json.dump(tasks, f)
        
    print("Task added successfully!")   
elif sys.argv[1] == "list": 
    with open(filename, "r") as p:
        tasks = json.load(p)
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"Task: {task['description']} | Status: {task['status']}")  

elif sys.argv[1] == "mark-done":
    task_id = int(sys.argv[2])
    with open(filename,"r") as d:
        tasks = json.load(d)
    for task in tasks:
        # Only check the ID if the ID key actually exists in this task
        if "id" in task and task["id"] == task_id:
            task["status"] = "done"
            print(f"Task {task_id} marked as done!")
            break
    with open(filename, "w") as d:
        json.dump(tasks,d)


if sys.argv[1] == "delete":
    task_id = int(sys.argv[2])
    with open (filename,"r") as f:
        tasks = json.load(f)
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            break
    with open(filename, "w") as f:
        json.dump(tasks, f)
        
