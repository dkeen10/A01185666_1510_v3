from unittest import TestCase
from unittest.mock import patch

from dnd import generate_syllable, generate_name


class TestGenerateName(TestCase):
    @patch("dnd.generate_syllable", side_effect=["ba"])
    def test_generate_name(self, mock_first_syllable):
        actual = generate_name(1)
        expected = "ba"
        self.assertEqual(actual, expected)

    @patch("dnd.generate_syllable", side_effect=["ro"])
    @patch("dnd.generate_syllable", side_effect=["ba"])
    def test_generate_name(self, mock_first_syllable, mock_second_syllable):
        actual = generate_name(2)
        expected = "baro"
        self.assertEqual(actual, expected)
