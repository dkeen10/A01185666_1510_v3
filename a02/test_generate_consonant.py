from unittest import TestCase
from unittest.mock import patch

from dnd import generate_consonant


class TestGenerateConsonant(TestCase):
    def test_generate_consonant_in_range(self):
        self.assertIn(generate_consonant(), ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s",
                                             "t", "v", "w", "x", "y", "z"])

    @patch('random.choice', side_effect=["d"])
    def test_generate_consonant(self, mock_rand_choice):
        actual = generate_consonant()
        self.assertEqual(actual, "d")
