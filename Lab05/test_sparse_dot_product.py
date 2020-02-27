from unittest import TestCase
from sparse_vector import sparse_dot_product

class Test(TestCase):
    def test_sparse_dot_product_different_lengths(self):
        actual = sparse_dot_product({'length': 6}, {'length': 5})
        expected = None
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_all_zeros(self):
        actual = sparse_dot_product({'length': 5}, {'length': 5})
        expected = 0
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_length_at_different_positions(self):
        actual = sparse_dot_product({'length': 5, 2: 7.5, 4: -6}, {4: -5, 'length': 5, 0: 4.3})
        expected = 30
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_same_location_opposite_magnitude(self):
        actual = sparse_dot_product({'length': 5, 2: -1}, {2: 1, 'length': 5})
        expected = -1
        self.assertEqual(expected, actual)
