import datetime

todo_list = []

def add_todo(task):
    todo_list.append(task)
    return f"Task added: {task}"

def show_todos():
    if not todo_list:
        return "Your to-do list is empty."
    return "Your tasks:\n" + "\n".join(f"{i+1}. {t}" for i, t in enumerate(todo_list))

def set_reminder(task, time_str):
    # Simple placeholder, real implementation would need scheduling
    return f"Reminder set for '{task}' at {time_str}."