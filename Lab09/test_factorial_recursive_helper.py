from unittest import TestCase
from factorial import factorial_recursive_helper


class TestFactorialRecursiveHelper(TestCase):
    def test_factorial_recursive_helper_four(self):
        test_num = 4
        actual = factorial_recursive_helper(test_num)
        expected = 24
        self.assertEqual(expected, actual)

    def test_factorial_recursive_helper_one(self):
        test_num = 1
        actual = factorial_recursive_helper(test_num)
        expected = 1
        self.assertEqual(expected, actual)

    def test_factorial_recursive_helper_zero(self):
        test_num = 0
        actual = factorial_recursive_helper(test_num)
        expected = 1
        self.assertEqual(expected, actual)
