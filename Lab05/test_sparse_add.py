from unittest import TestCase
from sparse_vector import sparse_add


class Test(TestCase):
    def test_sparse_add_different_lengths(self):
        actual = sparse_add({'length': 6}, {'length': 5})
        expected = None
        self.assertEqual(expected, actual)

    def test_sparse_add_all_zeros(self):
        actual = sparse_add({'length': 5}, {'length': 5})
        expected = {'length': 5}
        self.assertEqual(expected, actual)

    def test_sparse_add_length_at_different_positions(self):
        actual = sparse_add({'length': 5, 2: 7.5, 4: -6}, {4: -5, 'length': 5, 0: 4.3})
        expected = {'length': 5, 2: 7.5, 4: -11, 0: 4.3}
        self.assertEqual(expected, actual)

    def test_sparse_add_opposite_magnitude(self):
        actual = sparse_add({'length': 5, 2: -1}, {2: 1, 'length': 5})
        expected = {'length': 5}
        self.assertEqual(expected, actual)
