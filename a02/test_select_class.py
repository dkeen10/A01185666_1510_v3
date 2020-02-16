from unittest import TestCase
from unittest.mock import patch
import io

from dnd import select_class


class TestSelectClass(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=[1])
    def test_select_class_fighter(self, mock_input, mock_stdout):
        actual = select_class()
        expected = "fighter"
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    def test_select_class_each_class_once(self, mock_input, mock_stdout):
        roles = ["fighter", "paladin", "cleric", "monk", "barbarian", "rogue", "ranger", "bard", "druid", "wizard",
             "warlock", "sorcerer", ]
        for _ in range(12):
            role = select_class()
        self.assertIn(role, roles)



