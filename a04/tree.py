class Tree:
    """Represent a Tree."""

    def __init__(self, species: str, age: int, circumference: float):
        """Initialize new tree.

        :param species: a string
        :param age: an int
        :param circumference: a float
        :precondition: must give a non empty string and a positive int and float
        :postcondition: correctly initializes new tree
        :raise ValueError: if string is empty or numbers are negative

        >>> my_tree = Tree("Elm", 3, 55.5)
        >>> print(my_tree)
        3 year old tree of the Elm species with a circumference of 55.5 centimetres.
        """
        if not species.strip():
            raise ValueError("Tree cannot have an empty name")
        else:
            self.__species = species
        if age < 0:
            raise ValueError("The tree's age cannot be negative")
        else:
            self.__age = age
        if circumference < 0:
            raise ValueError("The tree's circumference cannot be zero!")
        else:
            self.__circumference = circumference

    def get_age(self) -> int:
        """Accessor for age of Tree object.

        :postcondition: age of Tree object has been successfully accessed
        :return: int of age

        >>> my_tree = Tree("Elm", 3, 55.5)
        >>> my_tree.get_age()
        3
        """
        return self.__age

    def get_circumference(self) -> float:
        """Accessor for circumference of Tree object.

        :postcondition: circumference of Tree object has been successfully accessed
        :return: float of circumference

        >>> my_tree = Tree("Elm", 3, 55.5)
        >>> my_tree.get_circumference()
        55.5
        """
        return self.__circumference

    def get_species(self) -> str:
        """Accessor for species of Tree object.

        :postcondition: species of Tree object has been successfully accessed
        :return: string of species

        >>> my_tree = Tree("Elm", 3, 55.5)
        >>> my_tree.get_species()
        'Elm'
        """
        return self.__species

    def set_circumference(self, new_circumference: float):
        """Mutator for circumference of Tree object.

        :param new_circumference: float
        :precondition: must give positive float for new circumference
        :postcondition: correctly updates circumference of tree
        :raise ValueError: if circumference is negative

        >>> my_tree = Tree("Elm", 3, 55.5)
        >>> my_tree.set_circumference(6.8)
        >>> my_tree.get_circumference()
        6.8
        """
        if new_circumference < 0:
            raise ValueError("THe tree's circumference cannot be negative")
        self.__circumference = new_circumference

    def set_age(self, new_age: int):
        """Mutator for circumference of Tree object.

        :param new_age: int
        :precondition: must give positive int for new age
        :postcondition: correctly updates age of tree
        :raise ValueError: if age is negative

        >>> my_tree = Tree("Elm", 3, 55.5)
        >>> my_tree.set_age(4)
        >>> my_tree.get_age()
        4
        """
        if new_age < 0:
            raise ValueError("THe tree's age cannot be negative")
        self.__age = new_age

    def __str__(self):
        """Return string that describes the tree.

        :return: string of tree description

        >>> my_tree = Tree("Pine", 4, 78.9)
        >>> str(my_tree)
        '4 year old tree of the Pine species with a circumference of 78.9 centimetres.'
        """

        return str(self.__age) + " year old tree of the " + self.__species + " species with a circumference of " + \
            str(self.__circumference) + " centimetres."

    def __repr__(self):
        """Return representational string that describes the tree object.

        :return: string representing tree.
        >>> my_tree = Tree("Pine", 4, 78.9)
        >>> repr(my_tree)
        'Tree("Pine", 4, 78.9)'
        """
        return "Tree(\"" + self.__species + "\", " + str(self.__age) + ", " + str(self.__circumference) + ")"
