# Problem Statement
**Numbered Task List**
- You’re improving the UX of a task management app by numbering the user’s task list automatically.

**Tasks:**
1. Define a function generate_numbered_tasks that takes a list of task names.
2. Use the enumerate() function to loop through the list with numbering starting from 1.
3. Format each task as "1. Task Name" and return the final list.

---
# Code
``` python
def generate_numbered_tasks(tasks: list[str]):
    for idx, item in enumerate(tasks, start=1):
        print(f"{idx}. {item}")


tasks = input("Enter your tasks (space separated).\n").split(" ")

generate_numbered_tasks(tasks)
```

---
