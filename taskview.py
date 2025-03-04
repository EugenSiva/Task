class TaskView:
    def display_tasks(self, tasks):
        print("\nÚlohy:")
        for task in tasks:
            status = "Hotovo" if task.is_completed else "Nedokončené"
            print(f"-{task.name} - {status}")