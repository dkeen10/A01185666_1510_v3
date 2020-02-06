from unittest import TestCase
from lab04 import eratosthenes


class TestEratosthenes(TestCase):
    def test_eratosthenes(self):
        """Test eratosthenes against a certain number."""
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], eratosthenes(30))

    def test_eratosthenes_lower_bound(self):
        """Test eratosthenes against lower bound."""
        self.assertEqual([], eratosthenes(0))
