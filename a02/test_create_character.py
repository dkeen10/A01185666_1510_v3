from unittest import TestCase
from unittest.mock import patch

from dnd import create_character, roll_die, generate_name, select_class, select_race


class TestCreateCharacter(TestCase):

    @patch("dnd.roll_die", side_effect=[14, 13, 6, 8, 18, 9, 3])
    @patch("dnd.select_race", side_effect=["human"])
    @patch("dnd.select_class", side_effect=["rogue"])
    @patch("dnd.generate_name", side_effect=["ba"])
    def test_create_character_d8(self, mock_name, mock_class, mock_race, mock_stats):
        actual = create_character(1)
        expected = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                    'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        self.assertEqual(actual, expected)


    @patch("dnd.roll_die", side_effect=[14, 13, 6, 8, 18, 9, 3])
    @patch("dnd.select_race", side_effect=["human"])
    @patch("dnd.select_class", side_effect=["wizard"])
    @patch("dnd.generate_name", side_effect=["ba"])
    def test_create_character_d6(self, mock_name, mock_class, mock_race, mock_stats):
        actual = create_character(1)
        expected = {'Name': 'ba', 'Class': 'wizard', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                    'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        self.assertEqual(actual, expected)

    @patch("dnd.roll_die", side_effect=[14, 13, 6, 8, 18, 9, 3])
    @patch("dnd.select_race", side_effect=["human"])
    @patch("dnd.select_class", side_effect=["fighter"])
    @patch("dnd.generate_name", side_effect=["ba"])
    def test_create_character_d10(self, mock_name, mock_class, mock_race, mock_stats):
        actual = create_character(1)
        expected = {'Name': 'ba', 'Class': 'fighter', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                    'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        self.assertEqual(actual, expected)

    @patch("dnd.roll_die", side_effect=[14, 13, 6, 8, 18, 9, 3])
    @patch("dnd.select_race", side_effect=["human"])
    @patch("dnd.select_class", side_effect=["rogue"])
    @patch("dnd.generate_name", side_effect=["ba"])
    def test_create_character_d12(self, mock_name, mock_class, mock_race, mock_stats):
        actual = create_character(1)
        expected = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                    'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        self.assertEqual(actual, expected)

    def test_create_character_no_syllables(self):
        actual = create_character(0)
        expected = None
        self.assertEqual(actual, expected)

