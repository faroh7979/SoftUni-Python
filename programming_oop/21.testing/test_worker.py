from unittest import TestCase, main


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTest(TestCase):

    def setUp(self):
        self.worker = Worker('Mane', 2000, 1)

    def test_initialization(self):
        self.assertEqual("Mane", self.worker.name)
        self.assertEqual(2000, self.worker.salary)
        self.assertEqual(1, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_increase_of_money_if_working(self):
        self.worker.work()
        self.assertEqual(2000, self.worker.money)

    def test_decrease_of_energy_when_working(self):
        self.worker.work()
        self.assertEqual(0, self.worker.energy)

    def test_is_raise_exception_in_case_of_zero_or_negative_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_is_energy_decrease_by_one(self):
        self.worker.rest()
        self.assertEqual(2, self.worker.energy)

    def test_get_info(self):
        get_info = self.worker.get_info()
        self.assertEqual('Mane has saved 0 money.', get_info)


if __name__ == '__main__':
    main()
