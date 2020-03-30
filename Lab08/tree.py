import doctest


class Tree:
    def __init__(self, species: str, age: int, circumference: float):
        """Initialize a Tree.

        :param species: a string
        :param age: a positive integer
        :param circumference: a positive float
        :precondition: species must be a string, age must be a positive integer, circumference must be a positive float
        :postcondition: the Tree object has been successfully initialized
        :raise ValueError: if species is an empty string
        :raise ValueError: if age is a negative integer
        :raise ValueError: if circumference is a negative float
        """
        if len(species.strip()):
            self.__species = species
        else:
            raise ValueError("species can't be blank!")

        if age >= 0:
            self.__age = age
        else:
            raise ValueError("age must be a positive integer!")

        if circumference >= 0:
            self.__circumference = circumference
        else:
            raise ValueError("circumference must be a positive number!")

    def get_species(self) -> str:
        """Accessor for the Tree object's species.

        :precondition: Tree is a well-formed Tree object
        :postcondition: correctly returns the Tree object's species
        :return: the Tree object's species

        >>> test_tree = Tree("redwood", 5, 50)
        >>> test_tree.get_species()
        'redwood'
        """
        return self.__species

    def get_age(self) -> int:
        """Accessor for the Tree object's age.

        :precondition: Tree is a well-formed Tree object
        :postcondition: correctly returns the Tree object's age
        :return: the Tree object's age

        >>> test_tree = Tree("redwood", 5, 50)
        >>> test_tree.get_age()
        5
        """
        return self.__age

    def get_circumference(self) -> float:
        """Accessor for the Tree object's circumference.

        :precondition: Tree is a well-formed Tree object
        :postcondition: correctly returns the Tree object's circumference
        :return: the Tree object's circumference

        >>> test_tree = Tree("redwood", 5, 50)
        >>> test_tree.get_circumference()
        50
        """
        return self.__circumference

    def set_species(self, species: str):
        """Mutator for the Tree object's species.

        :param species: a string
        :precondition: species cannot be an empty string, and the Tree object must be well-formed
        :postcondition: the Tree object's species has been successfully modified
        :raise ValueError: if species is an empty string

        >>> test_tree = Tree("redwood", 5, 50)
        >>> test_tree.set_species("oak")
        >>> test_tree.get_species()
        'oak'
        """
        if len(species.strip()):
            self.__species = species
        else:
            raise ValueError("species can't be blank!")

    def set_age(self, age: int):
        """Mutator for the Tree object's age

        :param age: a positive integer
        :precondition: age must be a positive integer, and the Tree object must be well-formed
        :postcondition: the Tree object's age has been successfully modified
        :raise ValueError: if age is a negative integer

        >>> test_tree = Tree("redwood", 5, 50)
        >>> test_tree.set_age(10)
        >>> test_tree.get_age()
        10
        """
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("age must be a positive integer!")

    def set_circumference(self, circumference: float):
        """Mutator for the Tree object's circumference

        :param circumference: a positive float
        :precondition: circumference must be a positive float, and the Tree object must be well-formed
        :postcondition: the Tree object's circumference has been successfully modified
        :raise ValueError: if circumference is a negative float

        >>> test_tree = Tree("redwood", 5, 50)
        >>> test_tree.set_circumference(70)
        >>> test_tree.get_circumference()
        70
        """
        if circumference >= 0:
            self.__circumference = circumference
        else:
            raise ValueError("circumference must be a positive number!")

    def __str__(self) -> str:
        """Return a string of the Tree object.

        :postcondition: correctly returns a string of the Tree object
        :return: a string of the tree object

        >>> test_tree = Tree("redwood", 5, 50)
        >>> print(test_tree)
        Species: redwood
        Age: 5 years
        Circumference: 50 centimetres
        """
        return f"Species: {self.__species}\nAge: {self.__age} years\nCircumference: {self.__circumference} centimetres"

    def __repr__(self) -> str:
        """Return a representational string of the Tree object.

        :postcondition: correctly returns the representational string of the Tree object
        :return: a representational string of the tree object

        >>> test_tree = Tree("redwood", 5, 50)
        >>> test_tree
        Species: redwood
        Age: 5 years
        Circumference: 50 centimetres
        """
        return f"Species: {self.__species}\nAge: {self.__age} years\nCircumference: {self.__circumference} centimetres"


def main():
    doctest.testmod()
    print(Tree("redwood", 50, 200))


if __name__ == "__main__":
    main()
