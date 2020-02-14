from unittest import TestCase
from unittest.mock import patch

from dnd import generate_syllable, generate_name,


class TestGenerateSyllable(TestCase):
    @patch("dnd.generate_vowel", side_effect=["a"])
    @patch("dnd.generate_consonant", side_effect=["b"])
    def test_generate_syllable_length(self, mock_consonant, mock_vowel):
        actual = generate_syllable()
        expected = 2
        self.assertEqual(len(actual), expected)

    @patch("dnd.generate_syllable", side_effect=["ro"])
    @patch("dnd.generate_syllable", side_effect=["ba"])
    def test_generate_syllable(self, mock_consonant, mock_vowel):
        actual = generate_syllable()
        expected = "baro"
        self.assertEqual(actual, expected)


    # @patch('random.choice', side_effect=["a"])
    # @patch()
    # def test_generate_syllable(self, mock_rand_choice):
    #     actual = generate_vowel()
    #     self.assertEqual(actual, "a")
