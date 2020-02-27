from unittest import TestCase
from sparse_vector import sparse_add


class Test(TestCase):
    def test_sparse_add_different_length_vectors(self):
        actual = sparse_add({'length': 6}, {'length': 5})
        expected = None
        self.assertEqual(expected, actual)

    def test_sparse_add_empty_vectors(self):
        actual = sparse_add({'length': 0}, {'length': 0})
        expected = None
        self.assertEqual(expected, actual)

    def test_sparse_add_zero_vectors(self):
        actual = sparse_add({'length': 1}, {'length': 1})
        expected = {'length': 1}
        self.assertEqual(expected, actual)

    def test_sparse_add_opposite_magnitude(self):
        actual = sparse_add({'length': 5, 2: -1}, {2: 1, 'length': 5})
        expected = {'length': 5}
        self.assertEqual(expected, actual)

    def test_sparse_add_mixed_length_sign_and_magnitude(self):
        actual = sparse_add({'length': 5, 2: 7, 4: -6}, {4: -5, 'length': 5, 0: 4})
        expected = {'length': 5, 2: 7, 4: -11, 0: 4}
        self.assertEqual(expected, actual)
