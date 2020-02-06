from unittest import TestCase
from lab04 import eratosthenes

"""
no tests for negative ints
test 0,1,2 (boundaries)
test a prime number (31, 47 ex.)
test an arbitrarily large number (ex.100)
"""
class TestEratosthenes(TestCase):
    def test_eratosthenes_prime(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31], eratosthenes(31))

    def test_eratosthenes_zero(self):
        self.assertEqual([], eratosthenes(0))

    def test_eratosthenes_one(self):
        self.assertEqual([], eratosthenes(0))

    def test_eratosthenes_two(self):
        self.assertEqual([], eratosthenes(0))

    def test_eratosthenes_non_prime(self):
        self.assertEqual([], eratosthenes(0))
