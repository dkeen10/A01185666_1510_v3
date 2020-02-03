import random


def roll_die():
    """
    asks user for number of rolls and number of sides of the die and returns the result
    :param number_of_rolls: number of die rolls
    :param number_of_sides: number of sides of the die
    :return: the result of the dice roll
    """
    number_of_rolls = int(input("how many rolls?"))
    number_of_sides = int(input("how many sides to your die?"))

    if number_of_sides > 1 and number_of_rolls > 0:
        dice_result = random.sample(range(number_of_rolls, number_of_sides * number_of_rolls + 1), 1)
        print("your result is " + str(dice_result))

    else:
        return 0


if __name__ == "__main__":
    roll_die()
