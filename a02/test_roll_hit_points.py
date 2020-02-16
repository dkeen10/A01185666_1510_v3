from unittest import TestCase
from unittest.mock import patch

from dnd import roll_hit_points, roll_die


class TestRollHitPoints(TestCase):
    @patch("dnd.roll_die", side_effect=[3])
    def test_roll_hit_points_for_d10(self, mock_roll):
        char = {'Name': 'ba', 'Class': 'fighter', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9}
        roll_hit_points(char)
        actual = char["HP"]
        expected = [3, 3]
        self.assertEqual(expected, actual)

    @patch("dnd.roll_die", side_effect=[3])
    def test_roll_hit_points_for_d8(self, mock_roll):
        char = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9}
        roll_hit_points(char)
        actual = char["HP"]
        expected = [3, 3]
        self.assertEqual(expected, actual)

    @patch("dnd.roll_die", side_effect=[3])
    def test_roll_hit_points_for_d6(self, mock_roll):
        char = {'Name': 'ba', 'Class': 'wizard', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9}
        roll_hit_points(char)
        actual = char["HP"]
        expected = [3, 3]
        self.assertEqual(expected, actual)

    @patch("dnd.roll_die", side_effect=[3])
    def test_roll_hit_points_for_d12(self, mock_roll):
        char = {'Name': 'ba', 'Class': 'barbarian', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9}
        roll_hit_points(char)
        actual = char["HP"]
        expected = [3, 3]
        self.assertEqual(expected, actual)
