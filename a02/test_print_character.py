from unittest import TestCase
from unittest.mock import patch
import io

from dnd import print_character


class TestPrintCharacter(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character(self, mock_stdout):
        print_character({'Name': 'lozy', 'Class': 'fighter', 'Race': 'human', 'Inventory': [], 'Experience': 0,
                         'Strength': 9, 'Dexterity': 14, 'Constitution': 12, 'Intelligence': 15, 'Wisdom': 10,
                         'Charisma': 11, 'HP': [4, 4]})
        expected = "Name lozy\nClass fighter\nRace human\nInventory []\nExperience 0\nStrength 9\nDexterity 14\n" \
                   "Constitution 12\nIntelligence 15\nWisdom 10\nCharisma 11\nHP [4, 4]\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
