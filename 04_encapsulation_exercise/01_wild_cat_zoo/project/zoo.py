from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: float) -> str:
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            found_worker = next(filter(lambda w: w.name == worker_name, self.workers))
            self.workers.remove(found_worker)

            return f"{worker_name} fired successfully"

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        workers_pay = sum([w.salary for w in self.workers])
        if self.__budget >= workers_pay:
            self.__budget -= workers_pay

            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        care_costs = sum([a.money_for_care for a in self.animals])
        if self.__budget >= care_costs:
            self.__budget -= care_costs

            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: float) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)} animals\n"
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]

        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += f"{lion}\n"

        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]

        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += f"{tiger}\n"

        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]

        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += f"{cheetah}\n"

        return result[:-1]

    def workers_status(self) -> str:
        result = f"You have {len(self.workers)} workers\n"
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]

        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += f"{keeper}\n"

        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]

        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += f"{caretaker}\n"

        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]

        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += f"{vet}\n"

        return result[:-1]
