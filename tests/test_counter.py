import unittest
from app.counter import DistributedCounter


class TestDistributedCounter(unittest.TestCase):
    def setUp(self):
        self.counter = DistributedCounter(['localhost:9092'], 'test_counter')

    def test_increment(self):
        initial_value = self.counter.get_value()
        self.counter.increment(5)
        self.assertEqual(self.counter.get_value(), initial_value + 5)

    def test_get_value(self):
        self.assertEqual(self.counter.get_value(), 0)


if __name__ == '__main__':
    unittest.main()
