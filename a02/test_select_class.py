from unittest import TestCase
from unittest.mock import patch
from random import randint
from dnd import select_class


class TestSelectClass(TestCase):
    @patch("builtins.input", side_effect=[1])
    def test_select_class_fighter(self, mock_input):
        actual = select_class()
        expected = "fighter"
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    def test_select_class_each_class_once(self, mock_input):
        roles = ["fighter", "paladin", "cleric", "monk", "barbarian", "rogue", "ranger", "bard", "druid", "wizard",
             "warlock", "sorcerer", ]
        for _ in range(12):
            role = select_class()
        self.assertIn(role, roles)



