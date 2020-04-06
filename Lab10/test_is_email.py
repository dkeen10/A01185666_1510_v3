from unittest import TestCase
from regular_expressions import is_email


class Test(TestCase):
    def test_is_email_simple_email(self):
        test_email = "duncankeen@gmail.com"
        expected = True
        actual = is_email(test_email)
        self.assertEqual(expected, actual)

    def test_is_email(self):
        test_email = "Henry nakamoto"
        expected = False
        actual = is_email(test_email)
        self.assertEqual(expected, actual)

