import doctest
import random
from random import randint


def roll_die(number_of_rolls, number_of_sides):
    i = 1
    dice_roll = 0
    while i <= number_of_rolls:
        dice_roll += randint(1, number_of_sides)
        i += 1
    return dice_roll


def generate_vowel():
    vowels = ["a", "e", "i", "o", "u", "y"]
    vowel = random.choice(vowels)
    return vowel


def generate_consonant():
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    consonant = random.choice(consonants)
    return consonant


def generate_syllable():
    syllable = generate_consonant() + generate_vowel()
    return syllable


def generate_name(syllables):
    name = ""
    if syllables > 1:
        for i in range(syllables):
            name += generate_syllable()
        return name
    else:
        print("None")


def select_class():
    roles = ["fighter", "paladin", "cleric", "monk", "barbarian", "rogue", "ranger", "bard", "druid", "wizard",
             "warlock", "sorcerer", ]
    for i, role in enumerate(roles, 1):
        print("%d: %s" % (i, role))
    role_number = int(input("Please select a class by choosing a number: (ex. if you want fighter, type 1)"))
    class_choice = roles[role_number-1]
    return class_choice


def select_race():
    races = ["human", "half-elf", "elf", "half-orc", "gnome", "halfling", "dwarf", "tiefling", "dragonborn"]
    for i, race in enumerate(races, 1):
        print("%d: %s" % (i, race))
    race_number = int(input("Please select a race by choosing a number: (ex. if you want human, type 1)"))
    race_choice = races[race_number-1]
    return race_choice


def create_character(syllables):
    if syllables > 1:
        inventory = []
        experience = 0

        character = {}
        character["Name"] = generate_name(2)
        character["class"] = select_class()
        character["race"] = select_race()
        character["Inventory"] = inventory
        character["Experience"] = experience
        character["strength"] = roll_die(3, 6)
        character["dexterity"] = roll_die(3, 6)
        character["constitution"] = roll_die(3, 6)
        character["intelligence"] = roll_die(3, 6)
        character["wisdom"] = roll_die(3, 6)
        character["charisma"] = roll_die(3, 6)

        if character["class"] in {"monk", "bard", "druid", "cleric", "rogue", "warlock"}:
            max_hp = roll_die(1, 8)
            character["HP"] = [max_hp, max_hp]
        elif character["class"] in {"fighter", "ranger", "paladin"}:
            max_hp = roll_die(1, 10)
            character["HP"] = [max_hp, max_hp]
        elif character["class"] in {"sorcerer", "wizard"}:
            max_hp = roll_die(1, 6)
            character["HP"] = [max_hp, max_hp]
        else:
            max_hp = roll_die(1, 12)
            character["HP"] = [max_hp, max_hp]

        print(character)
        return character
    else:
        print("")
        return None

#
#     #items method
#     for attribute, value in character_stats.items():
#         print(attribute, value)
#
#     #keys method (can also omit the .keys since it is the default search)
#     for key in character_stats.keys():
#         print(key, character_stats[key])
#
#
#     #values method (can be useful to invert dictionaries)


def print_character(character):
    print(character)


def choose_inventory():
    print("Welcome to Olgierd's!")
    print("")
    inventory = ["sword", "dagger", "bow", "wand of extend"]

    for i, item in enumerate(inventory, 1):
        print("%d: %s" % (i, item))
    item_number = int(input("Which item would you like to buy? (-1 to finish)"))
    item_choice = inventory[item_number - 1]
    print(item_choice)
    return item_choice


def main():
    # doctest.testmod()
    create_character(2)


if __name__ == "__main__":
    main()

# # initiative helper function
# # roll_to_hit function
# # roll_for_damage function
# # set life = False after life <0
# # enumerate for items list in store (lets you do 1: sword) (looks at slides)
