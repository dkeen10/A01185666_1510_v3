from unittest import TestCase
from unittest.mock import patch

from dnd import generate_vowel


class TestGenerateVowel(TestCase):
    def test_generate_vowel_in_range(self):
        for _ in range(100):
            self.assertIn(generate_vowel(), ["a", "e", "i", "o", "u", "y"])

    @patch('random.choice', side_effect=["a"])
    def test_generate_vowel_a(self, mock_rand_choice):
        actual = generate_vowel()
        self.assertEqual(actual, "a")

    def test_generate_vowel_100_times(self):
        letters = "aeiouy"
        for _ in range(100):
            letter = generate_vowel()
            self.assertTrue(letter in letters)
