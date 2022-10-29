from task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {Task.details(new_task)} is added to the section"

    def complete_task(self, task_name: str):
        current_index = self.tasks.index(task_name)
        if current_index == - 1:
            return f"Could not find task with the name {task_name}"

        self.tasks[current_index].completed = True
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
        list_for_returning = [f'Section {self.name}:\n']

        for new_element in self.tasks:
            list_for_returning.append(f'{new_element.details()}\n')

        return f'{"".join(list_for_returning)}'


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
