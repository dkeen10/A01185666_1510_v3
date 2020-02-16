from unittest import TestCase
from unittest.mock import patch

from dnd import choose_inventory


class TestChooseInventory(TestCase):
    @patch("builtins.input", side_effect=[-1])
    def test_choose_inventory_no_purchase(self, mock_input):
        character = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                     'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        choose_inventory(character)
        actual = character["Inventory"]
        expected = []
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=[1, -1])
    def test_choose_inventory_one_purchase(self, mock_input):
        character = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                     'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        choose_inventory(character)
        actual = character["Inventory"]
        expected = ["sword"]
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=[1, 1, -1])
    def test_choose_inventory_purchase_same_item_twice(self, mock_input):
        character = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                     'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        choose_inventory(character)
        actual = character["Inventory"]
        expected = ["sword", "sword"]
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=[1, 2, 3, 4, 5, -1])
    def test_choose_inventory_purchase_all_items_once(self, mock_input):
        character = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                     'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        choose_inventory(character)
        actual = character["Inventory"]
        expected = ["sword", "dagger", "bow", "staff", "potion of fire resistance"]
        self.assertEqual(actual, expected)
