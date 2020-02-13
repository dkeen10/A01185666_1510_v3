from unittest import TestCase
from unittest.mock import patch
import io

from dnd import print_character


class TestPrintCharacter(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character(self, mock_stdout):
        print_character({'Name': 'quti', 'class': 'fighter', 'race': 'human', 'Inventory': [], 'Experience': 0,
                         'strength': 9, 'dexterity': 14, 'constitution': 12, 'intelligence': 15, 'wisdom': 10,
                         'charisma': 11, 'HP': [4, 4]})
        expected = "Name lozy\nclass fighter\nrace human\nInventory []\nExperience 0\nstrength 12\ndexterity 4\n" \
                   "constitution 14\nintelligence 7\nwisdom 7\ncharisma 13\nHP [7, 7]\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
