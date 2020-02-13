from unittest import TestCase


class Test(TestCase):
    def test_combat_round(self):
        self.fail()

opponent_one = {'Name': 'wyba', 'Class': 'fighter', 'Race': 'human', 'Inventory': [], 'Experience': 0, 'Strength': 14,
                'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9, 'HP': [3, 3]}

opponent_two = {'Name': 'miraak', 'Class': 'barbarian', 'Race': 'dragonborn',
                'Inventory': ["Miraak's Staff", "Miraak's Sword"], 'Experience': 100, 'Strength': 12, 'Dexterity': 10,
                'constitution': 10, 'intelligence': 11, 'wisdom': 9, 'charisma': 8, 'HP': [7, 7]}
