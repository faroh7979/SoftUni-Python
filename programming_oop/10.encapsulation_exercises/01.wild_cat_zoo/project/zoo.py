from animal import Animal
from worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        try:
            searched_worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(searched_worker)
        return f'{worker_name} fired successfully'

    def pay_workers(self):
        budget_for_salary = 0
        for current_worker in self.workers:
            budget_for_salary += current_worker.salary

        if budget_for_salary <= self.__budget:
            self.__budget -= budget_for_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        budget_for_carrying = 0
        for current_animal in self.animals:
            budget_for_carrying += current_animal.money_for_care

        if budget_for_carrying <= self.__budget:
            self.__budget -= budget_for_carrying
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        final_return = [f'You have {len(self.animals)} animals']

        lions = list(filter(lambda a: a.__class__.__name__ == 'Lion', self.animals))
        tigers = list(filter(lambda a: a.__class__.__name__ == 'Tiger', self.animals))
        cheetahs = list(filter(lambda a: a.__class__.__name__ == 'Cheetah', self.animals))

        final_return.append(f'----- {len(lions)} Lions:')

        for lion in lions:
            final_return.append(lion.__repr__())

        final_return.append(f'----- {len(tigers)} Tigers:')

        for tiger in tigers:
            final_return.append(tiger.__repr__())

        final_return.append(f'----- {len(cheetahs)} Cheetahs:')

        for cheetah in cheetahs:
            final_return.append(cheetah.__repr__())

        return "\n".join(final_return)

    def workers_status(self):
        final_return = [f'You have {len(self.workers)} workers']

        keepers = list(filter(lambda w: w.__class__.__name__ == 'Keeper', self.workers))
        caretakers = list(filter(lambda w: w.__class__.__name__ == 'Caretaker', self.workers))
        vets = list(filter(lambda w: w.__class__.__name__ == 'Vet', self.workers))

        final_return.append(f'----- {len(keepers)} Keepers:')

        for keeper in keepers:
            final_return.append(keeper.__repr__())

        final_return.append(f'----- {len(caretakers)} Caretakers:')

        for caretaker in caretakers:
            final_return.append(caretaker.__repr__())

        final_return.append(f'----- {len(vets)} Vets:')

        for vet in vets:
            final_return.append(vet.__repr__())

        return "\n".join(final_return)


