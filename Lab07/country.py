import doctest


class Country:
    def __init__(self, name: str, population: int, area: int):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, country2) -> bool:
        """
        >>> canada = Country("Canada", 37_590_000, 9_985_000)
        >>> denmark = Country("Denmark", 5_603_000, 42_933)
        >>> canada.is_larger(denmark)
        True
        >>> denmark.is_larger(canada)
        False
        """
        if self.area > country2.area:
            return True
        else:
            return False

    def population_density(self) -> float:
        """
        >>> canada = Country("Canada", 37_590_000, 9_985_000)
        >>> canada.population_density()
        3.7646469704556833
        """
        population_density = self.population / self.area
        return population_density

    def __str__(self) -> str:
        """
        >>> canada = Country("Canada", 37_590_000, 9_985_000)
        >>> print(canada)
        Canada has a population of 37590000 and is 9985000 square kilometres.
        """
        return f"{self.name} has a population of {self.population} and is {self.area} square kilometres."

    def __repr__(self) -> str:
        """
        >>> canada = Country("Canada", 37_590_000, 9_985_000)
        >>> print(canada)
        Canada has a population of 37590000 and is 9985000 square kilometres.
        >>> canada
        <lab07_country.Country object at 0xaba7f255030b>
        >>> [canada]
        [<lab07_country.Country object at 0xaba7f255030b>]
        >>> print([canada])
        [<lab07_country.Country object at 0xaba7f255030b>]
        """
        # return f"{self.name} has a population of {self.population} and is {self.area} square kilometres."
        return '' + self.name + ' has a population of ' + str(self.population) + ' and is ' + str(self.area) + ' square kilometres.'


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
