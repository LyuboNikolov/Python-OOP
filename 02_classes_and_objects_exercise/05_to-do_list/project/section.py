from typing import List
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
            task.completed = True
            return f"Completed task {task_name}"

        except StopIteration:
            return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        removed_tasks = 0

        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                removed_tasks += 1

        return f"Cleared {removed_tasks} tasks."

    def view_section(self) -> str:
        details_joined = "\n".join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n{details_joined}"
