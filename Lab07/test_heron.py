from unittest import TestCase
from unittest.mock import patch
import io

from exceptions import heron


class TestHeron(TestCase):
    def test_heron_97(self):
        test_number = 97
        actual = heron(test_number)
        expected = 9.85
        self.assertEqual(actual, expected)

    def test_heron_9(self):
        test_number = 9
        actual = heron(test_number)
        expected = 3.00
        self.assertEqual(actual, expected)

    def test_heron_0(self):
        test_number = 0
        actual = heron(test_number)
        expected = 0
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_heron_negative_one(self, mock_stdout):
        test_number = -1
        actual = heron(test_number)
        expected = -1
        self.assertEqual(actual, expected)
        self.assertRaises(ZeroDivisionError)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_heron_negative_ninety_seven(self, mock_stdout):
        test_number = -97
        actual = heron(test_number)
        expected = -1
        self.assertEqual(actual, expected)
        self.assertRaises(ZeroDivisionError)
