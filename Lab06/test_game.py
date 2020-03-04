from unittest import TestCase
from unittest.mock import patch
import io
from maze import game, make_board, validate_move, move_character


class TestGame(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["E", "E", "E", "E", "S", "S", "S", "S"])
    def test_game_print_statements_ideal_path(self, mock_input, mock_stdout):
        game()
        actual = mock_stdout.getvalue()
        expected = """Current Location: [0, 0]
Current Location: [0, 1]
Current Location: [0, 2]
Current Location: [0, 3]
Current Location: [0, 4]
Current Location: [1, 4]
Current Location: [2, 4]
Current Location: [3, 4]
Congratulations! You've reached the end of the maze!
"""
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["E", "E", "E", "E", "S", "S", "S", "S"])
    def test_game_character_location(self, mock_input, mock_stdout):
        game()
        actual = character['Location']
        expected = [4, 4]
        self.assertEqual(expected, actual)
