from unittest import TestCase
from unittest.mock import patch

from dnd import select_race


class TestSelectClass(TestCase):
    @patch("builtins.input", side_effect=[1])
    def test_select_class(self, mock_input):
        actual = select_race()
        expected = "human"
        self.assertEqual(expected, actual)
