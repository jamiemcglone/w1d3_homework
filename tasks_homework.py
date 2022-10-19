tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# Print a list of uncompleted tasks

def uncompleted_tasks(tasks):
    uncompleted = []
    for i in range(len(tasks)):
        if tasks[i]["completed"] != True:
            uncompleted.append(tasks[i]["description"])
    return uncompleted

# Print a list of completed tasks

def completed_tasks(tasks):
    completed = []
    for i in range(len(tasks)):
        if tasks[i]["completed"]:
            completed.append(tasks[i]["description"])
    return completed


# Print a list of all task descriptions

def print_tasks(tasks):
    task_names = []
    for i in range(len(tasks)):
        task_names.append(tasks[i]["description"])
    return task_names

# Print a list of tasks where time_taken is at least a given time

def at_least_30(tasks):
    half_hour_tasks = []
    for i in range(len(tasks)):
        if tasks[i]["time_taken"] >= 30:
            half_hour_tasks.append(tasks[i]["description"])
    return half_hour_tasks

# Print any task with a given description

def print_wash_dishes(tasks):
    return(tasks[0]["description"])

print(tasks)
print(uncompleted_tasks(tasks))
print(completed_tasks(tasks))
print(print_tasks(tasks))
print(at_least_30(tasks))
print(print_wash_dishes(tasks))

# Extension

# Given a description update that task to mark it as complete.
def update_task(tasks, task_to_update):
    for i in range(len(tasks)):
        if tasks[i]["description"] == task_to_update:
            tasks[i]["completed"] = not tasks[i]["completed"]
    return tasks[i]

# Add a task to the list

def add_task(tasks, task_to_add):
    tasks.append(task_to_add)
    return tasks[-1]

print(update_task(tasks, "Feed Cat"))
print(add_task(tasks, {"description" : "Walk Cat", "completed" : False, "time_taken" : 300}))