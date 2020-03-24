from unittest import TestCase
from file_io import count_words
from collections import Counter


class TestCountWords(TestCase):
    def test_count_words_of_small_file(self):
        test_file = "test.txt"
        actual = count_words(test_file)
        expected = Counter({'test': 2, '123': 1})
        self.assertEqual(expected, actual)

    def test_count_words_of_empty_file(self):
        test_file = "test_empty.txt"
        actual = count_words(test_file)
        expected = Counter({})
        self.assertEqual(expected, actual)
