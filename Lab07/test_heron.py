from unittest import TestCase
from exceptions import heron

class Test(TestCase):
    def test_heron_97(self):
        test_number = 97
        actual = heron(97)
        expected = 9.84890052084378
        self.assertEqual(actual, expected)

    def test_heron_9(self):
        test_number = 9
        actual = heron(test_number)
        expected = 3.00
        self.assertEqual(actual, expected)

    def test_heron_0(self):
        test_number = 0
        actual = heron(test_number)
        expected = ValueError
        self.assertEqual(actual, expected)

    def test_heron_negative_one(self):
        test_number = -1
        actual = heron(test_number)
        expected = ValueError
        self.assertEqual(actual, expected)

    def test_heron_negative_nine(self):
        test_number = -9
        actual = heron(test_number)
        expected = ValueError
        self.assertEqual(actual, expected)
