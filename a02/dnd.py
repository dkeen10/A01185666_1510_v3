import doctest
import random
from random import randint
import itertools



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
    print("\nClasses:")
    for i, role in enumerate(roles, 1):
        print("%d: %s" % (i, role))
    role_number = int(input("Please select a class by choosing a number: (ex. if you want fighter, type 1)"))
    class_choice = roles[role_number-1]
    return class_choice


def select_race():
    races = ["human", "half-elf", "elf", "half-orc", "gnome", "halfling", "dwarf", "tiefling", "dragonborn"]
    print("\nRaces:")
    for i, race in enumerate(races, 1):
        print("%d: %s" % (i, race))
    race_number = int(input("Please select a race by choosing a number: (ex. if you want human, type 1)"))
    race_choice = races[race_number-1]
    return race_choice


def create_character(syllables):
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
    character_to_hit = character
    hit_roll = roll_die(1, 20)
    if hit_roll >= character_to_hit["dexterity"]:
        print(character_to_hit["Name"] + " has hit!")
        return True
    else:
        print(character_to_hit["Name"] + " missed!")
        return False


def combat_round(opponent_one, opponent_two):
    if roll_for_initiative():
        attacker = opponent_one
        defender = opponent_two
    else:
        attacker = opponent_two
        defender = opponent_one

    if roll_to_hit(attacker):
        alive = defender["HP"][1] - roll_for_damage(attacker)
        if alive <= 0:
            print(f"{defender['Name']} has died!")
        return defender["HP"][1]
    if defender["HP"][1] > 0:
        if roll_to_hit(defender):
            roll_for_damage(defender)
            alive = attacker["HP"][1] - roll_for_damage(defender)
            if alive <= 0:
                print(f"{attacker['Name']} has died!")
            return attacker["HP"][1]


    # i = roll_for_initiative()
    # alive = True
    # while alive:
    #     if i % 2 == 1:
    #         roll_to_hit(opponent_one.key(6))
    #         if roll_to_hit(opponent_one.key(6)):
    #             alive = opponent_two.key(11) - roll_for_damage(opponent_one)
    #             if alive <= 0:
    #                 print(f"{opponent_two.key(0)} has died!")
    #                 alive = False
    #         i += 1
    #     if i % 2 == 0:
    #         roll_to_hit(opponent_two.key(6))
    #         if roll_to_hit(opponent_two.key(6)):
    #             alive = opponent_one.key(11) - roll_for_damage(opponent_two)
    #             if alive <= 0:
    #                 print(f"{opponent_one} has died!")
    #                 alive = False
    #         i += 1
# 1 combat round -> p1 hits, p2 hits, or p1 hits, p2 misses, or p1,
# could assign opponent to victim, attacker
# if victim hasn't died, they get a chance to retaliate
# while opponent_one alive and opponent_two alive:
#


def main():
    # doctest.testmod()
    print("\nGreetings Traveller!\n")
    number_of_syllables = int(input("How many syllables is your name?"))
    main_character = create_character(number_of_syllables)
    print_character(main_character)
    choose_inventory(main_character)
    print(main_character)
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

# # initiative helper function
# # roll_to_hit function
# # roll_for_damage function
# # set life = False after life <0
# # enumerate for items list in store (lets you do 1: sword) (looks at slides)
