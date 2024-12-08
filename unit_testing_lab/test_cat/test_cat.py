from unittest import TestCase, main


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Maru")

    def test_correct_init(self):
        self.assertEqual("Maru", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eating_if_fed_should_return_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_cat_eats_should_be_fed_and_sleepy_and_increases_size(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_cat_sleeps_not_fed_should_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_sleeps_when_fed_should_return_sleepy_false(self):
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
