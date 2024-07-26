# view.py
class TaskView:
    def display_tasks(self, tasks):
        print("Tasks:")
        for task in tasks:
            print(f"- {task}")
