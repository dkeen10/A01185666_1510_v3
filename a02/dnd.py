import doctest
import random
from random import randint
# import itertools


def roll_die(number_of_rolls, number_of_sides):
    """Simulate rolling an any-sided die any number of times.

    :param number_of_rolls:
    :param number_of_sides:
    :precondition:
    :postcondition:
    :return:

    """
    i = 1
    dice_roll = 0
    while i <= number_of_rolls:
        dice_roll += randint(1, number_of_sides)
        i += 1
    return dice_roll


def generate_vowel():
    """Generate a random vowel.

    :precondition:
    :postcondition:
    :return: a random vowel
    """
    vowels = ["a", "e", "i", "o", "u", "y"]
    vowel = random.choice(vowels)
    return vowel


def generate_consonant():
    """Generate a random consonant.

    :precondition:
    :postcondition:
    :return:
    """
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y",
                  "z"]
    consonant = random.choice(consonants)
    return consonant


def generate_syllable():
    """Combine a random consonant and a random vowel into a consonant-vowel pair.

    :precondition:
    :postcondition:
    :return:
    """
    syllable = generate_consonant() + generate_vowel()
    return syllable


def generate_name(syllables):
    """Generate a random name.

    :param syllables:
    :precondition:
    :postcondition:
    :return:
    """
    name = ""
    if syllables > 1:
        for i in range(syllables):
            name += generate_syllable()
        return name
    else:
        print("None")


def select_class():
    """Prompt user to select a class from a list.

    :precondition:
    :postcondition:
    :return:

    """
    roles = ["fighter", "paladin", "cleric", "monk", "barbarian", "rogue", "ranger", "bard", "druid", "wizard",
             "warlock", "sorcerer", ]
    print("\nClasses:")
    for i, role in enumerate(roles, 1):
        print("%d: %s" % (i, role))
    role_number = int(input("Please select a class by choosing a number: (ex. if you want fighter, type 1)"))
    class_choice = roles[role_number-1]
    return class_choice


def select_race():
    """Prompt user to select a race from a list.

    :precondition:
    :postcondition:
    :return:
    """
    races = ["human", "half-elf", "elf", "half-orc", "gnome", "halfling", "dwarf", "tiefling", "dragonborn"]
    print("\nRaces:")
    for i, race in enumerate(races, 1):
        print("%d: %s" % (i, race))
    race_number = int(input("Please select a race by choosing a number: (ex. if you want human, type 1)"))
    race_choice = races[race_number-1]
    return race_choice


def create_character(syllables):
    """Create a character.

    :param syllables: a positive non-zero integer
    :precondition:
    :postcondition:
    :return:
    """
    if syllables >= 1:
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
            current_hp = max_hp
            character["HP"] = [max_hp, current_hp]
        elif character["class"] in {"fighter", "ranger", "paladin"}:
            max_hp = roll_die(1, 10)
            current_hp = max_hp
            character["HP"] = [max_hp, current_hp]
        elif character["class"] in {"sorcerer", "wizard"}:
            max_hp = roll_die(1, 6)
            current_hp = max_hp
            character["HP"] = [max_hp, current_hp]
        else:
            max_hp = roll_die(1, 12)
            current_hp = max_hp
            character["HP"] = [max_hp, current_hp]
        return character
    else:
        print("syllables must be a positive integer.")
        return None


def print_character(character):
    """Print a stylized text showing the user their created character.

    :precondition:
    :postcondition:
    """
    print("\n")
    print(r"                    ___====-_  _-====___                   ")
    print(r"              _--^^^#####//      \\#####^^^--_           ")
    print(r"           _-^##########// (    ) \\##########^-_           ")
    print(r"          -############//  |\^^/|  \\############-        ")
    print(r"        _/############//   (@::@)   \\############\_     ")
    print(r"       /#############((     \\//     ))#############\       ")
    print(r"      -###############\\    (oo)    //###############-         ")
    print(r"     -#################\\  / VV \  //#################-       ")
    print(r"    -###################\\/      \//###################-     ")
    print(r"    #/|##########/\######(   /\   )######/\##########|\#_       ")
    print(r"   |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|       ")
    print(r"   `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '       ")
    print(r"      `   `  `      `   / | |  | | \   '      '  '   '         ")
    print(r"                       (  | |  | |  )                       ")
    print(r"                      __\ | |  | | /__                     ")
    print(r"                     (vvv(VVV)(VVV)vvv)                       ")

    print("\nA new challenger has arrived, eager to face the Dragonlord! \n")
    for key in character.keys():
        print(key, character[key])


def choose_inventory(character):
    """Prompt user to choose items for their character's inventory.

    :param character:
    :precondition:
    :postcondition:
    :return:
    """
    print("\nIf you want to beat the Dragonlord, first you need some gear. Visit Olgierd's shop.")
    print("\n\nWelcome to Olgierd's!")
    print("\nWhat would you like to buy?\n")
    inventory = ["sword", "dagger", "bow", "potion of fire resistance"]
    item_number = 1
    while item_number > 0:
        for i, item in enumerate(inventory, 1):
            print("%d: %s" % (i, item))
        item_number = int(input("Which item would you like to buy? (-1 to finish)"))
        if item_number == -1:
            break
        item_choice = inventory[item_number - 1]
        del inventory[item_number - 1]
        character["Inventory"].append(item_choice)
        print(item_choice)
# could add a while loop if input outside of range of items


def roll_for_initiative():
    """Roll for who attacks first in a round of combat.

    :precondition:
    :postcondition:
    :return:
    """
    initiative1 = 0
    initiative2 = 0

    while initiative1 == initiative2:
        initiative1 = roll_die(1, 20)
        initiative2 = roll_die(1, 20)
    if initiative1 > initiative2:
        return True
    else:
        return False


def roll_for_damage(character):
    """Roll for damage dealt.

    :precondition:
    :postcondition:
    :return:
    """
    character_for_damage = character
    if character_for_damage["class"] in {"monk", "bard", "druid", "cleric", "rogue", "warlock"}:
        damage = roll_die(1, 8)
    elif character_for_damage["class"] in {"fighter", "ranger", "paladin"}:
        damage = roll_die(1, 10)
    elif character_for_damage["class"] in {"sorcerer", "wizard"}:
        damage = roll_die(1, 6)
    else:
        damage = roll_die(1, 12)
    print(character_for_damage["Name"] + f" dealt {damage} damage!")
    return damage


def roll_to_hit(character):
    """Roll to hit.

    :precondition:
    :postcondition:
    :return:
    """
    character_to_hit = character
    hit_roll = roll_die(1, 20)
    if hit_roll >= character_to_hit["dexterity"]:
        print(character_to_hit["Name"] + " has hit!")
        return True
    else:
        print(character_to_hit["Name"] + " missed!")
        return False


def combat_round(opponent_one, opponent_two):
    """Simulate one round of combat.

    :param opponent_one:
    :param opponent_two:
    :precondition:
    :postcondition:
    :return:
    """
    if roll_for_initiative():
        attacker = opponent_one
        defender = opponent_two
    else:
        attacker = opponent_two
        defender = opponent_one

    if roll_to_hit(attacker):
        defender["HP"][1] = defender["HP"][1] - roll_for_damage(attacker)
        if defender["HP"][1] <= 0:
            print(f"{defender['Name']} has died!")
        return defender["HP"][1]
    elif defender["HP"][1] > 0:
        if roll_to_hit(defender):
            attacker["HP"][1] = attacker["HP"][1] - roll_for_damage(defender)
            if attacker["HP"][1] <= 0:
                print(f"{attacker['Name']} has died!")
            return attacker["HP"][1]


def main():
    """Run the functions in this module.

    """
    # doctest.testmod()
    print("\nGreetings Traveller!\n")
    number_of_syllables = int(input("How many syllables is your name?"))
    main_character = create_character(number_of_syllables)
    print_character(main_character)
    choose_inventory(main_character)
    villain = {'Name': 'miraak', 'class': 'barbarian', 'race': 'dragonborn',
               'Inventory': ["Miraak's Staff", "Miraak's Sword"], 'Experience': 100, 'strength': 12, 'dexterity': 10,
               'constitution': 10, 'intelligence': 11, 'wisdom': 9, 'charisma': 8,
               'HP': [7, 7]}
    print("\nOh no! One of the Dragonlord's lieutenants has appeared. You must defeat him.\n")
    for key in villain.keys():
        print(key, villain[key])

    while True:
        i = input("Press enter to begin combat... ")
        if not i:
            while main_character["HP"][1] > 0 and villain["HP"][1] > 0:
                combat_round(main_character, villain)


if __name__ == "__main__":
    main()
