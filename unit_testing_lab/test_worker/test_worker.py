from unittest import TestCase, main

class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("Ivan", 100, 10)

    def test_correct_init(self):
        self.assertEqual("Ivan", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)

    def test_work_energy_0_or_less(self):
        self.worker.energy = -1

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_increase_salary(self):
        self.worker.work()

        self.assertEqual(100, self.worker.money)

    def test_decrease_energy(self):
        self.worker.work()

        self.assertEqual(9, self.worker.energy)

    def test_rest_should_increase_energy(self):
        self.worker.rest()

        self.assertEqual(11, self.worker.energy)

    def test_get_info(self):
        self.assertEqual(f"{self.worker.name} has saved {self.worker.money} money.", self.worker.get_info())

if __name__ == "__main__":
    main()