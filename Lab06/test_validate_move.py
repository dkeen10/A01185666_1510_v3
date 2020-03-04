from unittest import TestCase
from unittest.mock import patch
import io

from maze import validate_move, make_board


class TestValidateMove(TestCase):
    @patch('maze.game', side_effect=["tuba"])
    @patch('maze.make_board')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_not_in_NSEW(self, mock_stdout, board, direction):
        test_character = {"Location": [0, 0]}
        actual = validate_move(board, test_character, direction)
        expected = False
        self.assertEqual(expected, actual)

    @patch('maze.game', side_effect=["N"])
    @patch('maze.make_board')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_north_at_northern_edge(self, mock_stdout, board, direction):
        test_character = {"Location": [0, 0]}
        actual = validate_move(board, test_character, direction)
        expected = False
        self.assertEqual(expected, actual)

    @patch('maze.game', side_effect=["S"])
    @patch('maze.make_board')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_north_at_northern_edge(self, mock_stdout, board, direction):
        test_character = {"Location": [4, 0]}
        actual = validate_move(board, test_character, direction)
        expected = False
        self.assertEqual(expected, actual)

    @patch('maze.game', side_effect=["E"])
    @patch('maze.make_board')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_north_at_northern_edge(self, mock_stdout, board, direction):
        test_character = {"Location": [0, 4]}
        actual = validate_move(board, test_character, direction)
        expected = False
        self.assertEqual(expected, actual)

    @patch('maze.game', side_effect=["W"])
    @patch('maze.make_board')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_north_at_northern_edge(self, mock_stdout, board, direction):
        test_character = {"Location": [0, 0]}
        actual = validate_move(board, test_character, direction)
        expected = False
        self.assertEqual(expected, actual)

    @patch('maze.game', side_effect=["S"])
    @patch('maze.make_board')
    def test_validate_move_valid_move(self, board, direction):
        test_character = {"Location": [0, 0]}
        actual = validate_move(board, test_character, direction)
        expected = True
        self.assertEqual(expected, actual)
