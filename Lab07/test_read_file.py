from unittest import TestCase
from file_io import read_file

class TestReadFile(TestCase):
    def test_read_file(self):
        test_file = "abc"
        actual = read_file(test_file)
        expected = "abc"
        self.assertEqual(actual, expected)
