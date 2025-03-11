from taskcontroller import TaskController
from taskmodel import TaskModel
from taskview import TaskView

model = TaskModel()
view = TaskView()
controller = TaskController(model, view)

controller.add_task("Nakupit potraviny")
controller.add_task("Vyzdvihnut balik")
controller.add_task("Zavolaj Janovi")

controller.completed_task("Vyzdvihnut balik")

controller.display_tasks()

