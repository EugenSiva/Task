from taskmodel import Task

class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, name):
        task = Task(name)
        self.model.add_task(task)

    def completed_task(self, name):
        for task in self.model.get_tasks():
            if task.name == name:
                task.complete()

    def display_tasks(self):
        tasks = self.model.get_tasks()
        self.view.display_tasks(tasks)