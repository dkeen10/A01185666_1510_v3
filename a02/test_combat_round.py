from unittest import TestCase
from unittest.mock import patch

from dnd import combat_round, roll_for_initiative, roll_to_hit, roll_for_damage


class TestCombatRound(TestCase):
    @patch("roll_for_damage", side_effect=["wyba deals 3 damage!", 3])
    @patch("roll_to_hit", side_effect=["wyhba hits!", True])
    @patch("roll_for_initiative", side_effect=["wyba goes first!", True])
    def test_combat_round_opponent_one_deals_damage_opponent_two_misses(self, mock_initiative, mock_hit, mock_damage):
        opponent_one = {'Name': 'wyba', 'Class': 'fighter', 'Race': 'human', 'Inventory': [], 'Experience': 0,
                        'Strength': 14, 'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18,
                        'Charisma': 9, 'HP': [3, 3]}

        opponent_two = {'Name': 'miraak', 'Class': 'barbarian', 'Race': 'dragonborn',
                'Inventory': ["Miraak's Staff", "Miraak's Sword"], 'Experience': 100, 'Strength': 12, 'Dexterity': 10,
                'constitution': 10, 'intelligence': 11, 'wisdom': 9, 'charisma': 8, 'HP': [7, 7]}

        actual = combat_round(opponent_one, opponent_two)
        expected = """wyba goes first!
        wyba hits!  
        wyba deals 3 damage!
        miraak misses!"""
        self.assertEqual(actual, expected)

