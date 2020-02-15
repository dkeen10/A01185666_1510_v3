from unittest import TestCase
from unittest.mock import patch
import io

from dnd import roll_for_damage, roll_die


class TestRollForDamage(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dnd.roll_die", side_effect=[3])
    def test_roll_for_damage_d8(self, mock_roll_die, mock_stdout):
        character = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                     'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        roll_for_damage(character)
        actual = mock_stdout.getvalue()
        expected = "ba dealt 3 damage!\n"
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dnd.roll_die", side_effect=[3])
    def test_roll_for_damage_d10(self, mock_roll_die, mock_stdout):
        character = {'Name': 'ba', 'Class': 'fighter', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                     'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        roll_for_damage(character)
        actual = mock_stdout.getvalue()
        expected = "ba dealt 3 damage!\n"
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dnd.roll_die", side_effect=[3])
    def test_roll_for_damage_d6(self, mock_roll_die, mock_stdout):
        character = {'Name': 'ba', 'Class': 'wizard', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                     'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        roll_for_damage(character)
        actual = mock_stdout.getvalue()
        expected = "ba dealt 3 damage!\n"
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dnd.roll_die", side_effect=[3])
    def test_roll_for_damage_d12(self, mock_roll_die, mock_stdout):
        character = {'Name': 'ba', 'Class': 'barbarian', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                     'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        roll_for_damage(character)
        actual = mock_stdout.getvalue()
        expected = "ba dealt 3 damage!\n"
        self.assertEqual(expected, actual)
