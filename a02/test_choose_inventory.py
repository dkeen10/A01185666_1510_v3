from unittest import TestCase
from unittest.mock import patch
import io

from dnd import choose_inventory


class TestChooseInventory(TestCase):
    @patch("builtins.input", side_effect=[-1])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_choose_inventory_no_purchase(self, mock_stdout, mock_input):
        character = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                     'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        choose_inventory(character)
        actual = character["Inventory"]
        expected = []
        expected_print = """
If you want to beat the Dragonlord, first you need some gear. Visit Olgierd's shop.


Welcome to Olgierd's!
Here's what I have for sale:
1: sword
2: dagger
3: bow
4: staff
5: potion of fire resistance
"""
        self.assertEqual(actual, expected)
        self.assertEqual(mock_stdout.getvalue(), expected_print)
    # @patch("builtins.input", side_effect=[1, -1])
    # def test_choose_inventory_one_purchase(self, mock_input):
    #     character = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
    #                  'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
    #     choose_inventory(character)
    #     actual = character["Inventory"]
    #     expected = ["sword"]
    #     self.assertEqual(actual, expected)
    #
    # @patch("builtins.input", side_effect=[1, 1, -1])
    # def test_choose_inventory_purchase_same_item_twice(self, mock_input):
    #     character = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
    #                  'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
    #     choose_inventory(character)
    #     actual = character["Inventory"]
    #     expected = ["sword", "sword"]
    #     self.assertEqual(actual, expected)
    #
    # @patch("builtins.input", side_effect=[1, 2, 3, 4, 5, -1])
    # def test_choose_inventory_purchase_all_items_once(self, mock_input):
    #     character = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
    #                  'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
    #     choose_inventory(character)
    #     actual = character["Inventory"]
    #     expected = ["sword", "dagger", "bow", "staff", "potion of fire resistance"]
    #     self.assertEqual(actual, expected)
