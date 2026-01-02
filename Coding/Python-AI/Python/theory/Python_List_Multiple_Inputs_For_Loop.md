# Problem Statement
**Task Completion Tracker**
- **Instructions**
	- You’re building a simple task tracker for a to-do app. Whenever a user completes tasks, your app should mark them as done.  

**Tasks:**
1. Define a function mark_completed_tasks that accepts a list of task names.
2. Iterate through the list using a **for loop**, and update the format like "Completed:  {task}".
3. Return a new list with the updated task strings.

---
# Code
``` python
def mark_completed_tasks(tasks: list[str]):
    completed_tasks = []
    for task in tasks:
        completed_tasks.append(f"Completed: {task}")
    return completed_tasks


tasks = input("Enter tasks (space separated).\n").split(" ")

tasks_completed = mark_completed_tasks(tasks)
print(tasks_completed)
```

---
