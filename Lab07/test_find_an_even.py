from unittest import TestCase

from exceptions import find_an_even


class TestFindAnEven(TestCase):
    def test_find_an_even_one_even(self):
        test_list = [1, 2, 3]
        expected = 2
        actual = find_an_even(test_list)
        self.assertEqual(actual, expected)

    def test_find_an_even_zero(self):
        test_list = [0]
        expected = 0
        actual = find_an_even(test_list)
        self.assertEqual(actual, expected)

    def test_find_an_even_no_evens(self):
        test_list = [1, 3, 5]
        find_an_even(test_list)
        self.assertRaises(ValueError, msg="There were no evens input list")

    def test_find_an_even_empty_list(self):
        test_list = []
        find_an_even(test_list)
        self.assertRaises(ValueError, msg="There were no evens input list")
