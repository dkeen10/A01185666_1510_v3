def sum_of_calories(ingredient_list: dict) -> int:
    """Sum the calories of the ingredients in ingredient list.

    :param ingredient_list: a dictionary of ingredient:calories key value pairs
    :precondition: ingredient list must be a dictionary of ingredient:calories key value pairs
    :postcondition: the sum of the calories has been correctly calculated
    :return: the sum of the calories of the ingredients in ingredient_list
    """
    total_calories = 0
    for ingredient in ingredient_list:
        total_calories += ingredient_list[ingredient]
    return total_calories


def average_calories(total_calories: int, ingredient_list: dict) -> float:
    """Average calories of the ingredients in ingredient list.

    :param total_calories: an integer representing the total calories of the ingredients in ingredient_list
    :param ingredient_list: a dictionary of ingredient:calories key value pairs
    :precondition: total calories must be correctly calculated and ingredient_list must be a well-formed dictionary
    :return: the average calories of the ingredients in ingredient_list
    """
    avg_calories = total_calories / len(ingredient_list)
    return avg_calories


def print_ingredients(ingredient_list: dict):
    """Print the ingredients in ingredient list.

    :param ingredient_list: a dictionary of ingredient:calories key value pairs
    :precondition: ingredient list must be a dictionary of ingredient:calories key value pairs
    :postcondition: the ingredients in ingredient_list have been successfully printed
    """
    ingredient_names = []
    for ingredient in ingredient_list:
        ingredient_names.append(ingredient)
    print("\nIngredients:", sorted(ingredient_names))


def print_calories(total_calories: int, avg_calories: float):
    """Print the total and average calories of the ingredients in ingredient_list.

    :param total_calories: an integer representing the total calories of the ingredients in ingredient_list
    :param avg_calories: a float representing the average calories of the ingredients in ingredient_list
    :precondition: total_calories and avg_calories have been accurately calculated
    :postcondition: total_calories and avg_calories have been printed for the user
    """
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
