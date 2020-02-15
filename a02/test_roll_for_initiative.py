from unittest import TestCase
from unittest.mock import patch

from dnd import roll_for_initiative, roll_die


class TestRollForInitiative(TestCase):
    @patch("dnd.roll_die", side_effect=[20, 10])
    def test_roll_for_initiative_true(self, mock_roll_die):
        actual = roll_for_initiative()
        expected = True
        self.assertEqual(actual, expected)

    @patch("dnd.roll_die", side_effect=[10, 20])
    def test_roll_for_initiative_false(self, mock_roll_die):
        actual = roll_for_initiative()
        expected = False
        self.assertEqual(actual, expected)

    @patch("dnd.roll_die", side_effect=[10, 10, 10, 20])
    def test_roll_for_initiative_tie(self, mock_roll_die):
        actual = roll_for_initiative()
        expected = False
        self.assertEqual(actual, expected)
