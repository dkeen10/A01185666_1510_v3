from unittest import TestCase
from unittest.mock import patch
import io

from maze import validate_move, make_board


class TestValidateMove(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_not_in_NSEW(self, mock_stdout):
        mock_board = make_board()
        mock_character = {"Location": [2, 2]}
        mock_direction = "tuba"
        actual = validate_move(mock_board, mock_character, mock_direction)
        expected = False
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_north_at_northern_edge(self, mock_stdout):
        mock_board = make_board()
        mock_character = {"Location": [0, 0]}
        mock_direction = "N"
        actual = validate_move(mock_board, mock_character, mock_direction)
        expected = False
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_south_at_southern_edge(self, mock_stdout):
        mock_board = make_board()
        mock_character = {"Location": [4, 0]}
        mock_direction = "S"
        actual = validate_move(mock_board, mock_character, mock_direction)
        expected = False
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_east_at_eastern_edge(self, mock_stdout):
        mock_board = make_board()
        mock_character = {"Location": [0, 4]}
        mock_direction = "E"
        actual = validate_move(mock_board, mock_character, mock_direction)
        expected = False
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_west_at_western_edge(self, mock_stdout):
        mock_board = make_board()
        mock_character = {"Location": [0, 0]}
        mock_direction = "W"
        actual = validate_move(mock_board, mock_character, mock_direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_valid_move(self):
        mock_board = make_board()
        mock_character = {"Location": [0, 0]}
        mock_direction = "S"
        actual = validate_move(mock_board, mock_character, mock_direction)
        expected = True
        self.assertEqual(expected, actual)
