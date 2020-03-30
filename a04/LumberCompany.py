from tree import Tree
import TreeFarm


def print_interface():
    options = ["Add a tree", "Harvest one Tree", "Harvest some Trees", "Quit"]
    for i, item in enumerate(options, 1):
        print("%d. %s" % (i, item))


def user_input():
    return int(input(">>>"))


def choose_action(user_choice):
    if user_choice == 1:
        species = input("Which Species?")
        age = int(input("How old?"))
        circumference = int(input("What circumference?"))
        return Tree(species, age, circumference)
    elif user_choice == 2:
        diameter = input("What diameter?")
        print(diameter)
    elif user_choice == 3:
        diameter = input("What diameter?")
        print(diameter)
    elif user_choice == 4:
        pass
# def check_input(user_tree):


def main():
    print_interface()
    choose_action(user_input())

if __name__ == "__main__":
    main()
