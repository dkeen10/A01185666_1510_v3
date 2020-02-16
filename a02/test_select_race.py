from unittest import TestCase
from unittest.mock import patch
import io

from dnd import select_race


class TestSelectClass(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=[1])
    def test_select_race_human(self, mock_input, mock_stdout):
        actual = select_race()
        expected = "human"
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    def test_select_race_each_race_once(self, mock_input, mock_stdout):
        for _ in range(9):
            self.assertIn(select_race(), ["human", "half-elf", "elf", "half-orc", "gnome", "halfling", "dwarf",
                                          "tiefling", "dragonborn"])
