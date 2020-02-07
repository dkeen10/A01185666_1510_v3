from unittest import TestCase
from lab04 import eratosthenes


class TestEratosthenes(TestCase):
    def test_eratosthenes_prime(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31], eratosthenes(31))

    def test_eratosthenes_zero(self):
        self.assertEqual([], eratosthenes(0))

    def test_eratosthenes_one(self):
        self.assertEqual([], eratosthenes(1))

    def test_eratosthenes_two(self):
        self.assertEqual([2], eratosthenes(2))

    def test_eratosthenes_non_prime(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                          97], eratosthenes(100))
