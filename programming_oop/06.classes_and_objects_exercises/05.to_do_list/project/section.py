from task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):

        try:
            task_new = next(filter(lambda t: t.name == task_name, self.tasks))

        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task_new.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        removed_tasks = 0
        new_collection = []

        for element in self.tasks:
            if element.completed:
                removed_tasks += 1
            else:
                new_collection.append(element)

        self.tasks = new_collection
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        list_for_returning = [f'Section {self.name}:']

        [list_for_returning.append(t.details()) for t in self.tasks]

        return '\n'.join(list_for_returning)


