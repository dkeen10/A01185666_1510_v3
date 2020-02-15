from unittest import TestCase
from unittest.mock import patch

from dnd import roll_for_damage, roll_die


class TestRollForDamage(TestCase):
    @patch("dnd.roll_die", side_effect=[3])
    def test_roll_for_damage(self, mock_roll_die):
        character = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                     'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        actual = roll_for_damage(character)
        expected = "ba dealt 3 damage!\n"
        self.assertEqual(actual, expected)
