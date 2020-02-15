from unittest import TestCase
from unittest.mock import patch
import io

from dnd import roll_to_hit


class TestRollToHit(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dnd.roll_die", side_effect=[20])
    def test_roll_to_hit_has_hit(self, mock_roll_die, mock_stdout):
        char_one = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                     'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        char_two = {'Name': 'miraak', 'Class': 'barbarian', 'Race': 'dragonborn',
                'Inventory': ["Miraak's Staff", "Miraak's Sword"], 'Experience': 100, 'Strength': 12, 'Dexterity': 10,
                'constitution': 10, 'intelligence': 11, 'wisdom': 9, 'charisma': 8, 'HP': [7, 7]}
        roll_to_hit(char_one, char_two)
        expected = "ba has hit!\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dnd.roll_die", side_effect=[1])
    def test_roll_to_hit_missed(self, mock_roll_die, mock_stdout):
        char_one = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                     'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        char_two = {'Name': 'miraak', 'Class': 'barbarian', 'Race': 'dragonborn',
                'Inventory': ["Miraak's Staff", "Miraak's Sword"], 'Experience': 100, 'Strength': 12, 'Dexterity': 10,
                'constitution': 10, 'intelligence': 11, 'wisdom': 9, 'charisma': 8, 'HP': [7, 7]}
        roll_to_hit(char_one, char_two)
        expected = "ba missed!\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)