from unittest import TestCase
from unittest.mock import patch
import io

from dnd import combat_round, roll_for_initiative, roll_to_hit, roll_for_damage


class TestCombatRound(TestCase):
    @patch("dnd.roll_for_damage", side_effect=[3])
    @patch("dnd.roll_to_hit", side_effect=[True, False])
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dnd.roll_for_initiative", side_effect=[True])
    def test_combat_round_opponent_one_hits_and_damages_opponent_two_misses(self, mock_initiative, mock_stdout,
                                                                            mock_hit, mock_damage):
        opponent_one = {'Name': 'wyba', 'Class': 'fighter', 'Race': 'human', 'Inventory': [], 'Experience': 0,
                        'Strength': 14, 'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18,
                        'Charisma': 9, 'HP': [3, 3]}
        opponent_two = {'Name': 'miraak', 'Class': 'barbarian', 'Race': 'dragonborn',
                'Inventory': ["Miraak's Staff", "Miraak's Sword"], 'Experience': 100, 'Strength': 12, 'Dexterity': 10,
                'constitution': 10, 'intelligence': 11, 'wisdom': 9, 'charisma': 8, 'HP': [7, 7]}

        combat_round(opponent_one, opponent_two)
        expected_one = [3, 3]
        actual_one = opponent_one['HP']
        expected_two = [7, 4]
        actual_two = opponent_two['HP']

        self.assertEqual(expected_one, actual_one)
        self.assertEqual(expected_two, actual_two)

    @patch("dnd.roll_for_damage", side_effect=[3, 3])
    @patch("dnd.roll_to_hit", side_effect=[True, True])
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dnd.roll_for_initiative", side_effect=[True])
    def test_combat_round_opponent_one_hits_and_damages_opponent_two_hits_and_damages(self, mock_initiative,
                                                                                      mock_stdout, mock_hit,
                                                                                      mock_damage):
        opponent_one = {'Name': 'wyba', 'Class': 'fighter', 'Race': 'human', 'Inventory': [], 'Experience': 0,
                        'Strength': 14, 'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18,
                        'Charisma': 9, 'HP': [3, 3]}
        opponent_two = {'Name': 'miraak', 'Class': 'barbarian', 'Race': 'dragonborn',
                'Inventory': ["Miraak's Staff", "Miraak's Sword"], 'Experience': 100, 'Strength': 12, 'Dexterity': 10,
                'constitution': 10, 'intelligence': 11, 'wisdom': 9, 'charisma': 8, 'HP': [7, 7]}

        combat_round(opponent_one, opponent_two)
        expected_one = [3, 0]
        actual_one = opponent_one['HP']
        expected_two = [7, 4]
        actual_two = opponent_two['HP']

        self.assertEqual(expected_one, actual_one)
        self.assertEqual(expected_two, actual_two)

    @patch("dnd.roll_for_damage", side_effect=[3])
    @patch("dnd.roll_to_hit", side_effect=[True])
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dnd.roll_for_initiative", side_effect=[False])
    def test_combat_round_opponent_one_misses_opponent_two_hits_and_damages(self, mock_initiative,
                                                                                      mock_stdout, mock_hit,
                                                                                      mock_damage):
        opponent_one = {'Name': 'wyba', 'Class': 'fighter', 'Race': 'human', 'Inventory': [], 'Experience': 0,
                        'Strength': 14, 'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18,
                        'Charisma': 9, 'HP': [3, 3]}
        opponent_two = {'Name': 'miraak', 'Class': 'barbarian', 'Race': 'dragonborn',
                'Inventory': ["Miraak's Staff", "Miraak's Sword"], 'Experience': 100, 'Strength': 12, 'Dexterity': 10,
                'constitution': 10, 'intelligence': 11, 'wisdom': 9, 'charisma': 8, 'HP': [7, 7]}

        combat_round(opponent_one, opponent_two)
        expected_one = [3, 0]
        actual_one = opponent_one['HP']
        expected_two = [7, 7]
        actual_two = opponent_two['HP']

        self.assertEqual(expected_one, actual_one)
        self.assertEqual(expected_two, actual_two)

    @patch("dnd.roll_to_hit", side_effect=[False, False])
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("dnd.roll_for_initiative", side_effect=[False])
    def test_combat_round_opponent_one_misses_opponent_two_misses(self, mock_initiative, mock_stdout, mock_hit):
        opponent_one = {'Name': 'wyba', 'Class': 'fighter', 'Race': 'human', 'Inventory': [], 'Experience': 0,
                        'Strength': 14, 'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18,
                        'Charisma': 9, 'HP': [3, 3]}
        opponent_two = {'Name': 'miraak', 'Class': 'barbarian', 'Race': 'dragonborn',
                'Inventory': ["Miraak's Staff", "Miraak's Sword"], 'Experience': 100, 'Strength': 12, 'Dexterity': 10,
                'constitution': 10, 'intelligence': 11, 'wisdom': 9, 'charisma': 8, 'HP': [7, 7]}

        combat_round(opponent_one, opponent_two)
        expected_one = [3, 3]
        actual_one = opponent_one['HP']
        expected_two = [7, 7]
        actual_two = opponent_two['HP']

        self.assertEqual(expected_one, actual_one)
        self.assertEqual(expected_two, actual_two)
