from random import randint


def roll_die(number_of_rolls, number_of_sides):
    """Roll a die with the specified number of sides the specified number of times.

    :param number_of_rolls: a positive non-zero integer
    :param number_of_sides: a positive non-zero integer
    :precondition: number_of_rolls and number_of_sides must be positive non-zero integers
    :postcondition: generates a random dice role of the correct sided die being rolled the correct number of times
    :return: a correctly generated sum of the dice roll as an integer

    Computational Thinking:
    Decomposition: Dice rolls  are used throughout this module, so making a roll_die helper function that can be invoked
        wherever needed reduces repeated code.
    Abstraction: This function can roll an any-positive-integer-sided die any positive-integer-number of times.
    Algorithms: I used a for loop to generate the dice roll since that correctly randomizes the result for each time
        the die is rolled.
    """
    dice_roll = 0
    for i in range(0, number_of_rolls):
        dice_roll += randint(1, number_of_sides)
    return dice_roll

# def print_map():


def dungeon_map():
    rooms = ["You enter a throne room", "You enter an empty room with a chest", "You enter a dark hallway"]

    dungeon = {(0, 0): "", (0, 1): "", (0, 2): "", (0, 3): "", (0, 4): "",
               (1, 0): "", (1, 1): "", (1, 2): "", (1, 3): "", (1, 4): "",
               (2, 0): "", (2, 1): "", (2, 2): "", (2, 3): "", (2, 4): "",
               (3, 0): "", (3, 1): "", (3, 2): "", (3, 3): "", (3, 4): "",
               (4, 0): "", (4, 1): "", (4, 2): "", (4, 3): "", (4, 4): ""}

    for key in dungeon.keys():
        dungeon[key] = rooms[roll_die(1, 3) - 1]
    return dungeon


def movement_input(character, dungeon):
    direction = input("Move N, E, S, or W?")
    while direction not in {"N", "E", "S", "W"}:
        direction = input("Direction must be N, E, S, or W:")
    while direction == "N" and character["location"][0] == 0:
        direction = input("You are at the northern edge of the map! Enter a different direction:")
    while direction == "S" and character["location"][0] == 4:
        direction = input("You are at the southern edge of the map! Enter a different direction:")
    while direction == "E" and character["location"][1] == 4:
        direction = input("You are at the eastern edge of the map! Enter a different direction:")
    while direction == "W" and character["location"][1] == 0:
        direction = input("You are at the western edge of the map! Enter a different direction:")
    movement(direction, character, dungeon)


def movement(direction, character, dungeon):
    if direction == "N":
        character["location"][0] -= 1
    if direction == "S":
        character["location"][0] += 1
    if direction == "W":
        character["location"][1] -= 1
    if direction == "E":
        character["location"][1] += 1
    print(dungeon[tuple(character["location"])])
    # roll_for_encounter()


def heal_character(character):
    if character["HP"] < 10 and character["HP"] != 9:
        character["HP"] += 2
    elif character["HP"] == 9:
        character["HP"] += 1


# def roll_for_encounter():
#     if roll_die(1, 4) == 4:
#         combat_till_death()
#     else:
#         heal_character(character)


def main():
    main_char = {'Name': 'player', 'HP': 1, 'location': [2, 2]}
    dungeon = dungeon_map()
    while main_char['HP'] > 0:
        movement_input(main_char, dungeon)
        print(main_char)
        # print_map()


if __name__ == "__main__":
    main()
