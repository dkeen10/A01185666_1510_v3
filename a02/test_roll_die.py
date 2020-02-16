from unittest import TestCase
from unittest.mock import patch

from dnd import roll_die


class TestRollDie(TestCase):
    def test_roll_one_sided_die_once(self):
        for _ in range(100):
            expected = 1
            actual = roll_die(1, 1)
            self.assertEqual(expected, actual)

    def test_roll_six_sided_die_once(self):
        for _ in range(100):
            actual = roll_die(1, 6)
            self.assertGreaterEqual(actual, 1)
            self.assertLessEqual(actual, 6)

    def test_roll_six_sided_die_twice(self):
        for _ in range(100):
            actual = roll_die(2, 6)
            self.assertGreaterEqual(actual, 2)
            self.assertLessEqual(actual, 12)

    def test_roll_ten_sided_die_ten_times(self):
        # can also do assertInRange
        for _ in range(100):
            actual = roll_die(10, 10)
            self.assertGreaterEqual(actual, 10)
            self.assertLessEqual(actual, 100)

    @patch('random.randint', side_effect=[3])
    def test_roll_die_roll_once(self, mock_randint):
        actual = roll_die(3, 3)
        expected = 3
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 1, 1])
    # parameters are inverted: closest patch to the function is the first, and furthest is the last
    def test_roll_die_roll_three_times(self, mock_randint):
        actual = roll_die(3, 1)
        expected = 3
        self.assertEqual(expected, actual)
