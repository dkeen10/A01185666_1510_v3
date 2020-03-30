from unittest import TestCase
from tree import Tree


class TestTree(TestCase):
    def setUp(self):
        self.test_tree = Tree("redwood", 5, 50)

    def test_get_species(self):
        actual = self.test_tree.get_species()
        expected = "redwood"
        self.assertEqual(actual, expected)

    def test_get_age(self):
        actual = self.test_tree.get_age()
        expected = 5
        self.assertEqual(actual, expected)

    def test_get_circumference(self):
        actual = self.test_tree.get_circumference()
        expected = 50
        self.assertEqual(actual, expected)

    def test_set_species(self):
        self.test_tree.set_species("oak")
        actual = self.test_tree.get_species()
        expected = "oak"
        self.assertEqual(actual, expected)

    def test_set_species_with_empty_species(self):
        with self.assertRaises(ValueError):
            self.test_tree.set_species("")

    def test_set_age(self):
        self.test_tree.set_age(10)
        actual = self.test_tree.get_age()
        expected = 10
        self.assertEqual(actual, expected)

    def test_set_age_with_negative_age(self):
        with self.assertRaises(ValueError):
            self.test_tree.set_age(-10)

    def test_set_circumference(self):
        self.test_tree.set_circumference(75)
        actual = self.test_tree.get_circumference()
        expected = 75
        self.assertEqual(actual, expected)

    def test_set_age_with_negative_circumference(self):
        with self.assertRaises(ValueError):
            self.test_tree.set_circumference(-75)

    def test_init_empty_species(self):
        with self.assertRaises(ValueError):
            Tree("", 5, 50)

    def test_init_negative_age(self):
        with self.assertRaises(ValueError):
            Tree("redwood", -5, 50)

    def test_init_negative_circumference(self):
        with self.assertRaises(ValueError):
            Tree("redwood", 5, -50)

    def test_str(self):
        expected = """Species: redwood
Age: 5 years
Circumference: 50 centimetres"""
        actual = self.test_tree.__str__()
        self.assertEqual(expected, actual)

    def test_repr_string(self):
        expected = """Species: redwood
Age: 5 years
Circumference: 50 centimetres"""
        actual = self.test_tree.__repr__()
        self.assertEqual(expected, actual)
