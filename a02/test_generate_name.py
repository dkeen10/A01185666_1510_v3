from unittest import TestCase
from unittest.mock import patch

from dnd import generate_syllable, generate_name


class TestGenerateName(TestCase):
    @patch("dnd.generate_syllable", side_effect=["ba"])
    def test_generate_name_one_syllable(self, mock_first_syllable):
        actual = generate_name(1)
        expected = "ba"
        self.assertEqual(actual, expected)

    @patch("dnd.generate_syllable", side_effect=["ba", "ro"])
    def test_generate_name_two_syllables(self, mock_first_syllable):
        actual = generate_name(2)
        expected = "baro"
        self.assertEqual(actual, expected)
