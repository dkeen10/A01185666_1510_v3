from unittest import TestCase
from country import Country


class TestCountry(TestCase):
    def setUp(self):
        self.test_country = Country("Canada", 37_590_000, 9_985_000)
        self.test_country_2 = Country("Denmark", 5_603_000, 42_933)

    def test_is_larger_True(self):
        expected = True
        actual = self.test_country.is_larger(self.test_country_2)
        self.assertEqual(expected, actual)

    def test_is_larger_False(self):
        expected = False
        actual = self.test_country_2.is_larger(self.test_country)
        self.assertEqual(expected, actual)

    def test_population_density(self):
        expected = 3.7646469704556833
        actual = self.test_country.population_density()
        self.assertEqual(expected, actual)

    def test___str__(self):
        expected = "Canada has a population of 37590000 and is 9985000 square kilometres."
        actual = self.test_country.__str__()
        self.assertEqual(expected, actual)

    def test___repr___string(self):
        expected = "Canada has a population of 37590000 and is 9985000 square kilometres."
        actual = self.test_country.__repr__()
        self.assertEqual(expected, actual)

    def test___repr___list(self):
        expected = ["Canada has a population of 37590000 and is 9985000 square kilometres."]
        actual = [self.test_country.__repr__()]
        self.assertEqual(expected, actual)
