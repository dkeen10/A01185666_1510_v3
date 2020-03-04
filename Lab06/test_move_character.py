from unittest import TestCase
from unittest.mock import patch
import io

from maze import move_character


class TestMoveCharacter(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_move_character_south(self, mock_stdout):
        test_character = {'Location': [0, 0]}
        test_direction = "S"
        move_character(test_direction, test_character)
        actual = test_character["Location"]
        expected = [1, 0]
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_move_character_east(self, mock_stdout):
        test_character = {'Location': [0, 0]}
        test_direction = "E"
        move_character(test_direction, test_character)
        actual = test_character["Location"]
        expected = [0, 1]
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_move_character_north(self, mock_stdout):
        test_character = {'Location': [1, 1]}
        test_direction = "N"
        move_character(test_direction, test_character)
        actual = test_character["Location"]
        expected = [0, 1]
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_move_character_west(self, mock_stdout):
        test_character = {'Location': [1, 1]}
        test_direction = "W"
        move_character(test_direction, test_character)
        actual = test_character["Location"]
        expected = [1, 0]
        self.assertEqual(expected, actual)
