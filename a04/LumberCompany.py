import doctest

from tree import Tree
from TreeFarm import TreeFarm


def user_input() -> int:
    """Get user input.

    :postcondition: user has successfully entered their choice from the interface
    :raise ValueError: if user_inp is outside of 1-4
    :return: the user's input, else 0 if ValueError is raised
    """
    try:
        user_inp = int(input(">>>"))
        if not 1 <= user_inp <= 4:
            raise ValueError("choice must be within 1-4")
    except ValueError:
        print("please enter a choice between 1-4")
        return 0
    return user_inp


def print_interface():
    """Print the interface for users to interact with the TreeFarm.

    :postcondition: the interface has been successfully printed

    >>> print_interface()
    1. Add a tree
    2. Harvest one Tree
    3. Harvest some Trees
    4. Quit
    """
    options = ["Add a tree", "Harvest one Tree", "Harvest some Trees", "Quit"]
    for i, item in enumerate(options, 1):
        print("%d. %s" % (i, item))


def check_add(farm):
    """Add a new Tree to the Tree Farm.

    :param farm: a well-formed TreeFarm
    :precondition: farm must be a well-formed TreeFarm
    :postcondition: the TreeFarm has been successfully modified to include the new Tree
    :raise ValueError: if species contains an empty string
    :raise ValueError: if age is not a positive, non-zero integer
    :raise ValueError: if circumference is not a positive, non-zero float
    :return: the modified TreeFarm with the new Tree added, else nothing if ValueError is raised
    """
    species = input("What species is the tree?")
    age = int(input("How old is the tree? (in years)"))
    circumference = float(input("What circumference is the tree? (in cm)"))
    try:
        if not len(species):
            raise ValueError("Species can't be empty")
        elif age <= 0:
            raise ValueError("age must be a positive non-zero integer")
        elif circumference <= 0:
            raise ValueError("circumference must be a positive non-zero integer")
    except ValueError as e:
        print(f"Error occurred: {e}")
        return
    else:
        new_tree = Tree(species, age, circumference)
        farm.add(new_tree)
        return farm


def check_remove_tree(farm):
    """Remove a tree from the Tree Farm.

    :param farm: a well-formed TreeFarm object
    :precondition: farm must a well-formed TreeFarm
    :postconddition: correctly removes the specified tree from the TreeFarm
    :raise ValueError: if circumference is not a positive, non-zero integer
    :return: the TreeFarm with the specified Tree removed
    """
    circumference = float(input("What circumference of tree would you like? (in cm)"))
    if circumference <= 0:
        raise ValueError("Circumference must a positive, non-zero integer")
    print(f"Tree harvested: {farm.remove_tree(circumference)}")
    return farm.remove_tree(circumference)


def check_remove_trees(farm):
    """Remove trees with circumference greater than specified value from the Tree Farm.

    :param farm: a well-formed TreeFarm object
    :precondition: farm must a well-formed TreeFarm
    :postconddition: correctly removes the specified trees from the TreeFarm
    :raise ValueError: if circumference is not a positive, non-zero integer
    :return: the TreeFarm with the specified Trees removed
    """
    circumference = float(input("What circumference of trees would you like? (in cm)"))
    if circumference <= 0:
        raise ValueError("Circumference must a positive, non-zero integer")
    print(f"Trees harvested: {farm.remove_trees(circumference)}")
    return farm.remove_trees(circumference)


def choose_action(user_choice: int, farm):
    """Handle user input.

    :param user_choice: user input in the form of an integer between 1 and 4
    :param farm: a well formed TreeFarm object
    :precondition: user_choice must be an integer between 1 and 4 (inclusive) and farm must be a well-formed TreeFarm
    :postcondition: correctly modifies the TreeFarm based on user_input
    :raise ValueError: if circumference input is negative
    :raise ValueError: if circumference input is negative
    :return: the modified TreeFarm based on user_input
    """

    if user_choice == 1:
        check_add(farm)
    elif user_choice == 2:
        try:
            check_remove_tree(farm)
        except ValueError:
            print("You must enter a positive circumference")
    elif user_choice == 3:
        try:
            check_remove_trees(farm)
        except ValueError:
            print("You must enter a positive circumference")
    elif user_choice == 4:
        return


def main():
    doctest.testmod()
    farm = TreeFarm()
    user_inp = None
    while user_inp != 4:
        print_interface()
        user_inp = user_input()
        if user_inp != 4:
            choose_action(user_inp, farm)
            if len(farm.get_tree_list()):
                print("Tree Farm contains:")
            farm.print_trees()


if __name__ == "__main__":
    main()
