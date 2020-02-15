from unittest import TestCase
from unittest.mock import patch
import io

from dnd import roll_to_hit


class TestRollToHit(TestCase):

    def test_roll_to_hit_hit(self):
        character = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                     'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        roll_to_hit(character)

    def test_roll_to_hit_miss(self):
        character = {'Name': 'ba', 'Class': 'rogue', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                     'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}
        roll_to_hit(character)