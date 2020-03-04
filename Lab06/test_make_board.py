from unittest import TestCase
from maze import make_board


class TestMakeBoard(TestCase):
    def test_make_board(self):
        actual = make_board()
        expected = {(0, 0): False, (1, 0): False, (2, 0): False, (3, 0): False, (4, 0): False, (0, 1): False,
                    (1, 1): False, (2, 1): False, (3, 1): False, (4, 1): False, (0, 2): False, (1, 2): False,
                    (2, 2): False, (3, 2): False, (4, 2): False, (0, 3): False, (1, 3): False, (2, 3): False,
                    (3, 3): False, (4, 3): False, (0, 4): False, (1, 4): False, (2, 4): False, (3, 4): False,
                    (4, 4): True}
        self.assertEqual(expected, actual)
