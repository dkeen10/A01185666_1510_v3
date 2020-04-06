from unittest import TestCase
from regular_expressions import is_nakamoto


class Test(TestCase):
    def test_is_nakamoto_True(self):
        test_name = "Henry Nakamoto"
        expected = True
        actual = is_nakamoto(test_name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_Nakamoto_not_capitalized(self):
        test_name = "Henry nakamoto"
        expected = False
        actual = is_nakamoto(test_name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_first_name_not_capitalized(self):
        test_name = "henry Nakamoto"
        expected = False
        actual = is_nakamoto(test_name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_one_letter_first_name(self):
        test_name = "H Nakamoto"
        expected = True
        actual = is_nakamoto(test_name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_punctuation_in_first_name(self):
        test_name = "H. Nakamoto"
        expected = False
        actual = is_nakamoto(test_name)
        self.assertEqual(expected, actual)

    def test_is_nakamoto_no_first_name(self):
        test_name = "Nakamoto"
        expected = False
        actual = is_nakamoto(test_name)
        self.assertEqual(expected, actual)
