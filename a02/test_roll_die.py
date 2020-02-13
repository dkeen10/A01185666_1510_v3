from unittest import TestCase
from unittest.mock import patch

from dnd import roll_die


class TestRollDie(TestCase):
    def test_roll_one_sided_die_once(self):
        expected = 1
        actual = roll_die(1, 1)
        self.assertEqual(expected, actual)

    def test_roll_six_sided_die_once(self):
        actual = roll_die(1, 6)
        self.assertGreaterEqual(actual, 1)
        self.assertLessEqual(actual, 6)

    def test_roll_six_sided_die_twice(self):
        actual = roll_die(2, 6)
        self.assertGreaterEqual(actual, 2)
        self.assertLessEqual(actual, 12)

    def test_roll_ten_sided_die_ten_times(self):
        # can also do assertInRange
        actual = roll_die(10, 10)
        self.assertGreaterEqual(actual, 10)
        self.assertLessEqual(actual, 100)

    @patch('random.randint', side_effect=[3])
    def test_roll_die_roll_once(self, mock_randint):
        actual = roll_die(3, 3)
        self.assertEqual(actual, 3)

    @patch('random.randint', side_effect=[3, 2, 1])
    @patch('random.choice', side_effect=[3, 2, 1])
    # parameters are inverted: closest patch to the function is the first, and furthest is the last
    def test_roll_die_roll_twice(self, mock_rand_choice, mock_randint):
        actual = roll_die(3, 3)
        self.assertEqual(actual, 3)
