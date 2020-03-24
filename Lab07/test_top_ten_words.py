from unittest import TestCase
from unittest.mock import patch
import io

from file_io import top_ten_words


class TestTopTenWords(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_top_ten_words_alice(self, mock_stdout):
        test_file = "gutenberg/alice.txt"
        top_ten_words(test_file)
        expected = """the: 1804
and: 912
to: 801
a: 684
of: 625
it: 541
she: 538
said: 462
you: 429
in: 428
"""
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_top_ten_words_moby_dick(self, mock_stdout):
        test_file = "gutenberg/moby_dick.txt"
        top_ten_words(test_file)
        expected = """the: 14507
of: 6701
and: 6434
a: 4690
to: 4658
in: 4202
that: 2955
his: 2520
it: 2382
i: 1943
"""
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_top_ten_words_little_women(self, mock_stdout):
        test_file = "gutenberg/little_women.txt"
        top_ten_words(test_file)
        expected = """and: 8097
the: 7681
to: 5148
a: 4509
of: 3518
her: 3245
i: 3144
in: 2500
it: 2470
she: 2279
"""
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_top_ten_words_siddhartha(self, mock_stdout):
        test_file = "gutenberg/siddhartha.txt"
        top_ten_words(test_file)
        expected = """the: 2219
and: 1426
to: 1225
of: 1106
a: 968
he: 936
his: 708
in: 686
had: 524
was: 512
"""
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_top_ten_words_empty_doc(self, mock_stdout):
        test_file = "test_empty.txt"
        top_ten_words(test_file)
        expected = """"""
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
