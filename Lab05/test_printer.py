"""
Demonstrate how to mock an object.
"""

from unittest import TestCase

import unittest.mock # NEW
import io # NEW

import printing_functions


class TestMyPrinter(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_my_printer(self, mock_stdout):
        printing_functions.my_printer("Hello world!")
        expected = "Hello world!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)


