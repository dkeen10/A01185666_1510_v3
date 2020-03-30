"""
refactoring_calories.py

This program initializes a dictionary, and then repeatedly prompts the user
for new food items and their associated calories. The new items are added
to the dictionary. Each time an item is added, the list of foods is printed
along with total and average calories.

The program works as is, and contains no bugs.

Unfortunately this program is just written as one big script, and is not very
well organized. It needs to use Functions like we have discussed in class, a
proper command loop, and unit tests to prove everything works.

Your tasks:

1. Refactor this program so that it is composed of short, atomic, and
   re-usable functions
2. Add a suite of unit tests that prove everything works as it should.
"""


def sum_of_calories(ingredient_list):
    total_calories = 0
    for ingredient in ingredient_list:
        total_calories += ingredient_list[ingredient]
    return total_calories


def average_calories(total_calories, ingredient_list):
    avg_calories = total_calories / len(ingredient_list)
    return avg_calories


def print_ingredients(ingredient_list):
    ingredient_names = []
    for ingredient in ingredient_list:
        ingredient_names.append(ingredient)
    print("\nIngredients:", sorted(ingredient_names))


def print_calories(total_calories, avg_calories):
    print("Total Calories:", total_calories,
          "Average Calories: %0.1f\n" % avg_calories)


def main():
    ingredient_list = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,
                       "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
                       "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}

    new_ingredient = input("Enter food item to add, or 'q' to exit: ")
    while new_ingredient != "q":
        new_ingredient_calories = int(input(f"Enter calories for {new_ingredient}:"))
        ingredient_list[new_ingredient] = new_ingredient_calories
        print_ingredients(ingredient_list)
        calorie_sum = sum_of_calories(ingredient_list)
        print_calories(calorie_sum, average_calories(calorie_sum, ingredient_list))
        new_ingredient = input("Enter food item to add, or 'q' to exit: ")


if __name__ == "__main__":
    main()
