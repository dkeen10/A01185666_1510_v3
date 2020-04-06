from unittest import TestCase
from regular_expressions import is_email


class Test(TestCase):
    def test_is_email_valid_gmail(self):
        test_email = "duncankeen@gmail.com"
        expected = True
        actual = is_email(test_email)
        self.assertEqual(expected, actual)

    def test_is_email_valid_hotmail(self):
        test_email = "duncankeen@hotmail.ca"
        expected = True
        actual = is_email(test_email)
        self.assertEqual(expected, actual)

    def test_is_email_valid_username_with_underscore(self):
        test_email = "duncan_keen@hotmail.ca"
        expected = True
        actual = is_email(test_email)
        self.assertEqual(expected, actual)

    def test_is_email_no_username(self):
        test_email = "@gmail.com"
        expected = False
        actual = is_email(test_email)
        self.assertEqual(expected, actual)

    def test_is_email_invalid_username_with_dash(self):
        test_email = "duncan-10@gmail.com"
        expected = False
        actual = is_email(test_email)
        self.assertEqual(expected, actual)

    def test_is_email_invalid_username_with_dot(self):
        test_email = "duncan.keen@gmail.com"
        expected = False
        actual = is_email(test_email)
        self.assertEqual(expected, actual)

    def test_is_email_no_domain(self):
        test_email = "duncankeen@.com"
        expected = False
        actual = is_email(test_email)
        self.assertEqual(expected, actual)

    def test_is_email_invalid_domain(self):
        test_email = "duncankeen@gm$ail.com"
        expected = False
        actual = is_email(test_email)
        self.assertEqual(expected, actual)

    def test_is_email_no_top_level_domains(self):
        test_email = "duncankeen@gmail"
        expected = False
        actual = is_email(test_email)
        self.assertEqual(expected, actual)

    def test_is_email_too_many_top_level_domains(self):
        test_email = "duncankeen@gmail.com.my"
        expected = False
        actual = is_email(test_email)
        self.assertEqual(expected, actual)

    def test_is_email_too_short_top_level_domain(self):
        test_email = "duncankeen@gmail.c"
        expected = False
        actual = is_email(test_email)
        self.assertEqual(expected, actual)

    def test_is_email_missing_at_sign(self):
        test_email = "duncankeengmail.com"
        expected = False
        actual = is_email(test_email)
        self.assertEqual(expected, actual)

    def test_is_email_missing_period_after_domain(self):
        test_email = "duncankeen@gmailcom"
        expected = False
        actual = is_email(test_email)
        self.assertEqual(expected, actual)
