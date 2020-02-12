from unittest import TestCase
from unittest.mock import patch

"""
Demonstrate how to mock an object.
"""

import user_input


class TestAskForValueAndConvertToLower(TestCase):

    @patch('builtins.input', side_effect=["  2qt4wrdz  "])
    def test_ask_for_value_and_convert_to_lower(self, mock_input):
        actual = user_input.ask_for_value_and_convert_to_upper()
        expected = "2QT4WRDZ"
        self.assertEqual(expected, actual)

