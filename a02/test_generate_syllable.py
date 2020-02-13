from unittest import TestCase
from unittest.mock import patch

from dnd import generate_syllable, generate_vowel, generate_consonant


class TestGenerateSyllable(TestCase):
    @patch(generate_vowel(), side_effect="a")
    @patch(generate_consonant(), side_effect="b")
    def test_generate_syllable_length(self, mock_consonant, mock_vowel):
        actual = generate_syllable()
        self.assertEqual(len(actual), 2)

    @patch(generate_vowel(), side_effect="a")
    @patch(generate_consonant(), side_effect="b")
    def test_generate_syllable(self, mock_consonant, mock_vowel):
        actual = generate_syllable()
        self.assertEqual(actual, "ba")


    # @patch('random.choice', side_effect=["a"])
    # @patch()
    # def test_generate_syllable(self, mock_rand_choice):
    #     actual = generate_vowel()
    #     self.assertEqual(actual, "a")
