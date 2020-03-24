from unittest import TestCase
from file_io import read_file


class TestReadFile(TestCase):
    def test_read_file(self):
        test_file = "test.txt"
        actual = read_file(test_file)
        expected = "test test 123"
        self.assertEqual(actual, expected)
