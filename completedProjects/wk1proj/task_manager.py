# 
""""
project: Task manager
Strength:

About:
- use list of dicts to store tasks

functions
   - Adding tasks  
   - Viewing tasks  
   - Marking tasks as done  
   - Deleting tasks  
   - Saving/loading tasks from a file  

"""


import json

# File to store tasks
task_file = "tasks.json"

# Load tasks from file (if exists)
def load_tasks():
    try:
        with open(task_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(task_file, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "❌"
        print(f"{index}. {task['task']} [{status}]")

# Mark a task as done
def complete_task(task_index):
    tasks = load_tasks()
    if 0 < task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(task_index):
    tasks = load_tasks()
    if 0 < task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task['task']}")
    else:
        print("Invalid task number.")

# Main CLI loop
def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            task_index = int(input("Enter task number to mark as done: "))
            complete_task(task_index)
        elif choice == "4":
            view_tasks()
            task_index = int(input("Enter task number to delete: "))
            delete_task(task_index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()