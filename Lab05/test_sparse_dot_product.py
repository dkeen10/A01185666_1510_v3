from unittest import TestCase
from sparse_vector import sparse_dot_product


class Test(TestCase):
    def test_sparse_dot_product_different_length_vectors(self):
        actual = sparse_dot_product({'length': 6}, {'length': 5})
        expected = None
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_empty_vectors(self):
        actual = sparse_dot_product({'length': 0}, {'length': 0})
        expected = None
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_zero_vectors(self):
        actual = sparse_dot_product({'length': 1}, {'length': 1})
        expected = 0
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_length_at_different_positions(self):
        actual = sparse_dot_product({'length': 5, 2: 7, 4: -6}, {4: -5, 'length': 5, 0: 4})
        expected = 30
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_all_magnitudes_at_different_positions(self):
        actual = sparse_dot_product({'length': 5, 1: -1, 3: 2}, {0: 4, 2: 1, 'length': 5, 4: 3})
        expected = 0
        self.assertEqual(expected, actual)
