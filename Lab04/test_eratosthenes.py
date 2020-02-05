from unittest import TestCase
from lab04 import eratosthenes


class TestEratosthenes(TestCase):
    def test_eratosthenes(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], eratosthenes(30))
