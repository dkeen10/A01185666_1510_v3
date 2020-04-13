from tree import Tree


class TreeFarm:
    """Represents a farm of trees."""

    def __init__(self):
        """Initializes a new tree farm."""
        self.__tree_list = []

    def get_tree_list(self):
        """Accessor for the tree list.

        :postcondition: correctly returns the Trees in TreeFarm
        :return: The list of Trees currently in TreeFarm

        >>> my_farm = TreeFarm()
        >>> my_farm.get_tree_list()
        []
        >>> elm = Tree("Elm", 12, 56.5)
        >>> my_farm = TreeFarm()
        >>> my_farm.add(elm)
        >>> my_farm.get_tree_list()
        [Tree("Elm", 12, 56.5)]
        >>> elm = Tree("Elm", 12, 56.5)
        >>> oak = Tree("oak", 10, 50)
        >>> my_farm = TreeFarm()
        >>> my_farm.add(elm)
        >>> my_farm.add(oak)
        >>> my_farm.get_tree_list()
        [Tree("Elm", 12, 56.5), Tree("oak", 10, 50)]
        """
        return self.__tree_list

    def add(self, new_tree: object):
        """Add a tree to the tree farm.

        :param new_tree: an object
        :precondition: must give a Tree object
        :postcondition: correctly adds tree to the farm.
        :raise TypeError: if not given a tree

        >>> elm = Tree("Elm", 12, 56.5)
        >>> my_farm = TreeFarm()
        >>> my_farm.add(elm)
        >>> my_farm.print_trees()
        Tree Species: Elm Age: 12
        """
        if isinstance(new_tree, Tree):
            self.__tree_list.append(new_tree)
        else:
            raise TypeError("Not a Tree")

    def print_trees(self):
        """Print trees in tree farm.

        :precondition: call the method
        :postcondition: prints age and species of every tree in the farm

        >>> pine = Tree("Pine", 8, 56.5)
        >>> my_farm = TreeFarm()
        >>> my_farm.add(pine)
        >>> my_farm.print_trees()
        Tree Species: Pine Age: 8
        """
        for tree in self.__tree_list:
            print("Tree Species: " + tree.get_species() + " Age: " + str(tree.get_age()))

    def remove_tree(self, circumference: float):
        """Remove tree from farm.

        :param circumference: float of circumference
        :precondition: must give float for circumference
        :postcondition: removes tree from the farm that have greater or equal circumference than given.
        :return: tree object that has been removed.

        >>> my_farm = TreeFarm()
        >>> my_farm.add(Tree("Pine", 8, 56.5))
        >>> my_farm.remove_tree(50.0)
        Tree("Pine", 8, 56.5)
        """
        for tree in self.__tree_list[:]:
            if tree.get_circumference() >= circumference:
                self.__tree_list.remove(tree)
                return tree
        return None

    def remove_trees(self, circumference: float):
        """Remove multiple trees from farm

        :param circumference: float of circumference
        :precondition: must give float for circumference
        :postcondition: removes trees from the farm that have a greater or equal circumference than given.
        :return: list of tree that have been removed.

        >>> my_farm = TreeFarm()
        >>> my_farm.add(Tree("Pine", 8, 56.5))
        >>> my_farm.add(Tree("Elm", 8, 56.5))
        >>> my_farm.add(Tree("Oak", 8, 34.5))
        >>> my_farm.remove_trees(50.0)
        [Tree("Pine", 8, 56.5), Tree("Elm", 8, 56.5)]
        """
        removed_trees = [tree for tree in self.__tree_list if tree.get_circumference() >= circumference]
        for tree in removed_trees:
            self.__tree_list.remove(tree)
        if not removed_trees:
            return None
        return removed_trees
