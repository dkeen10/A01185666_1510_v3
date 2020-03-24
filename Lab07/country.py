import doctest


class Country:
    def __init__(self, name: str, population: int, area: int):
        """Initialize the Country Class.

        :param name: a string
        :param population: an integer
        :param area: an integer
        :precondition: name must a string, population and area must be integers
        :postcondition: a country has been initialized
        :Raise ValueError: if name is empty
        :Raise ValueError: if populations is negative
        :Raise ValueError: if area is negative
        """
        if len(name):
            self.name = name
        else:
            raise ValueError("name cant be empty")

        if population > 0:
            self.population = population
        else:
            raise ValueError("population must be an integer greater than zero")

        if area > 0:
            self.area = area
        else:
            raise ValueError("area must be an integer greater than zero")

    def is_larger(self, country2) -> bool:
        """Determine if the specified country is larger than another specified country.

        :param country2: a country
        :precondition: country2 must be a well formed country
        :postcondition: correctly returns True if country is greater than country2, else False.
        :return: True if country is greater than country2, else False.

        >>> canada = Country("Canada", 37_590_000, 9_985_000)
        >>> denmark = Country("Denmark", 5_603_000, 42_933)
        >>> canada.is_larger(denmark)
        True
        >>> denmark.is_larger(canada)
        False
        """
        return self.area > country2.area

    def population_density(self) -> float:
        """Find the population density of the specified country.

        :postcondition: returns the correct the population density of the specified country
        :return: the population density of the specified country

        >>> canada = Country("Canada", 37_590_000, 9_985_000)
        >>> canada.population_density()
        3.7646469704556833
        """
        population_density = self.population / self.area
        return population_density

    def __str__(self) -> str:
        """Print a string of the country.

        :Postcondition: a string of the country has been printed.
        >>> canada = Country("Canada", 37_590_000, 9_985_000)
        >>> print(canada)
        Canada has a population of 37590000 and is 9985000 square kilometres.
        """
        return f"{self.name} has a population of {self.population} and is {self.area} square kilometres."

    def __repr__(self) -> str:
        """Print a representational string of the Country.

        :postcondition: correctly returns the representational string of the country
        :return: the representational string of the country

        >>> canada = Country("Canada", 37_590_000, 9_985_000)
        >>> print(canada)
        Canada has a population of 37590000 and is 9985000 square kilometres.
        >>> canada
        Country("Canada", 37590000, 9985000)
        >>> [canada]
        [Country("Canada", 37590000, 9985000)]
        """
        return 'Country("' + str(self.name)+'", ' + str(self.population) + ', ' + str(self.area)+ ')'


def main():
    doctest.testmod()
    canada = Country("Canada", 37_590_000, 9_985_000)
    denmark = Country("Denmark", 5_603_000, 42_933)

    print(canada.population_density())
    print(denmark.is_larger(canada))
    print(canada)
    print(canada.__str__())
    print(canada.__repr__())


if __name__ == "__main__":
    main()
