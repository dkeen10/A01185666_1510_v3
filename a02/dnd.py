import doctest
import random
from random import randint


def roll_die(number_of_rolls, number_of_sides):
    """Roll a die with the specified number of sides the specified number of times.

    Computational Thinking:
    Decomposition: Dice rolls  are used throughout this module, so making a roll_die helper function that can be invoked
        wherever needed reduces repeated code.
    Abstraction: This function can roll an any-positive-integer-sided die any positive-integer-number of times.
    Algorithms: I used a for loop to generate the dice roll since that correctly randomizes the result for each time
        the die is rolled.

    :param number_of_rolls: a positive non-zero integer
    :param number_of_sides: a positive non-zero integer
    :precondition: number_of_rolls and number_of_sides must be positive non-zero integers
    :postcondition: generates a random dice role of the correct sided die being rolled the correct number of times
    :return: a correctly generated sum of the dice roll as an integer
    """
    dice_roll = 0
    for i in range(0, number_of_rolls):
        dice_roll += randint(1, number_of_sides)
    return dice_roll


def generate_vowel():
    """Generate a random vowel.

    Computational Thinking:
    Decomposition: This is a helper function to generate_syllable
    Abstraction: This same method of generating a list, then choosing a random element from the list is also used in
        generate_consonant, and can be used for get random choices for other applications.

    :postcondition: a random vowel has been chosen from a list of vowels
    :return: a random vowel
    """
    vowels = ["a", "e", "i", "o", "u", "y"]
    vowel = random.choice(vowels)
    return vowel


def generate_consonant():
    """Generate a random consonant.

    Computational Thinking:
    Decomposition: This is a helper function to generate_syllable
    Abstraction: This same method of generating a list, then choosing a random element from the list is also used in
        generate_vowel, and can be used for get random choices for other applications.

    :postcondition:a random consonant has been chosen from a list of consonants
    :return: a random consonant
    """
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y",
                  "z"]
    consonant = random.choice(consonants)
    return consonant


def generate_syllable():
    """Combine a random consonant and a random vowel into a consonant-vowel pair.

    Computational Thinking:
    Decomposition: I used the generate syllable helper function to reduce repeated code. The generate syllable helper
        function then uses the generate_consonant and generate_vowel helper functions to generate a syllable.
    Algorithms: I used a for loop to populate an empty string with syllables consisting of consonant-vowel pairs up
        to the specified number of syllables.

    :postcondition: correctly generates a consonant-vowel pair of a random consonant and a random vowel
    :return: a correctly generated consonant-vowel pair of a random consonant and a random vowel
    """
    syllable = generate_consonant() + generate_vowel()
    return syllable


def generate_name(syllables):
    """Generate a random name.

    Computational Thinking:
    Decomposition: This function was functionally decomposed by using the helper function generate syllable.
        In addition, this function is itself a helper function to create_character.
    Algorithms: a for loop was used to populate the name with consonant-vowel pairs up to the number of syllables.

    :param syllables: a positive non-zero integer
    :precondition: syllables must be a positive non-zero integer
    :postcondition: generates a random name of the specified number of syllables
    :return: a randomly generated name of the specified number of syllables
    """
    name = ""
    for i in range(int(syllables)):
        name += generate_syllable()
    return name


def select_class():
    """Prompt user to select a class from a list.

    Computational Thinking:
    Decomposition: This is a helper function to the create_character function
    Abstraction: This enumerate method is also used in select_race and choose_inventory and is a good way to present
        lists in a more user friendly way.
    Algorithms: The enumerate function was used to display the list of classes in a more user-friendly way, as well as
        allow for the user to make a selection by typing in the integer relating to the class instead of having to type
        in the whole class name.

    :precondition: this function will only work if user selects a number from the list
    :postcondition: the user has chosen a class
    :return: the user's chosen class
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

    Computational Thinking:
    Decomposition: This is a helper function to the create_character function
    Abstraction: This enumerate method is also used in select_class and choose_inventory and is a good way to present
        lists in a more user friendly way.
    Algorithms: The enumerate function was used to display the list of classes in a more user-friendly way, as well as
        allow for the user to make a selection by typing in the integer relating to the class instead of having to type
        in the whole class name.

    :precondition: this function will only work if user selects a number from the list
    :postcondition: the user has chosen a race
    :return: the user's chosen race
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

    Computational Thinking:
    Decomposition: This populates an empty dictionary using several helper functions, including generate_name,
        select_class, select_race, and roll_die
    Pattern Matching: Since multiple classes all use the same-sided die to roll for HP, I grouped them in lists when
        calculating the HP of the user's character.
    Abstraction: this function works for any input of syllables.  By using if statements, the function runs if syllables
        is an integer greater than zero, or prints an error message and returns None if syllables is zero or a negative
         integer, or even if it is not an integer at all.

    :param syllables: a positive non-zero integer
    :precondition: syllables must be a positive non-zero integer, or anything else to get a helpful error message
    :postcondition: a correctly created character in
    :return: a correctly created character in, or None if syllables was in the incorrect form
    """
    try:    # create_character first tries this set of code.
        if int(syllables) > 0:
            inventory = []
            experience = 0

            character = {}     # i am purposefully not writing this as a dictionary literal so it has better readability
            character["Name"] = generate_name(syllables)
            character["Class"] = select_class()
            character["Race"] = select_race()
            character["Inventory"] = inventory
            character["Experience"] = experience
            character["Strength"] = roll_die(3, 6)
            character["Dexterity"] = roll_die(3, 6)
            character["Constitution"] = roll_die(3, 6)
            character["Intelligence"] = roll_die(3, 6)
            character["Wisdom"] = roll_die(3, 6)
            character["Charisma"] = roll_die(3, 6)

            if character["Class"] in {"monk", "bard", "druid", "cleric", "rogue", "warlock"}:
                max_hp = roll_die(1, 8)
                current_hp = max_hp
                character["HP"] = [max_hp, current_hp]
            elif character["Class"] in {"fighter", "ranger", "paladin"}:
                max_hp = roll_die(1, 10)
                current_hp = max_hp
                character["HP"] = [max_hp, current_hp]
            elif character["Class"] in {"sorcerer", "wizard"}:
                max_hp = roll_die(1, 6)
                current_hp = max_hp
                character["HP"] = [max_hp, current_hp]
            else:
                max_hp = roll_die(1, 12)
                current_hp = max_hp
                character["HP"] = [max_hp, current_hp]
            return character
        else:       # if syllables is a float or an integer less than or equal to zero:
            print("syllables must be a positive integer.")
            return None
    except ValueError:      # if the function gets a ValueError because of syllables' datatype, it instead does this:
        print("syllables must be a positive integer.")
        return None


def print_dragon():
    r"""Print an ascii art dragon.

    Computational Thinking
    Decomposition: Originally, this function was in the main.  I created this helper function and evoked it in the main
        to make the main more readable while still keeping the lore.
    Pattern Matching: instead of doing prints statements for each each, I did one print statement with triple quotes.
        However, the backslashes in the ascii art were causing issues.  I then realized I could do a raw triple quote
        for the print statement as well as for the docstring itself so that the doctest would work.

    :postcondition: a correctly printed ascii art dragon

    >>> print_dragon()
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
                            ___====-_  _-====___
                      _--^^^#####//      \\#####^^^--_
                   _-^##########// (    ) \\##########^-_
                  -############//  |\^^/|  \\############-
                _/############//   (@::@)   \\############\_
               /#############((     \\//     ))#############\
              -###############\\    (oo)    //###############-
             -#################\\  / VV \  //#################-
            -###################\\/      \//###################-
            #/|##########/\######(   /\   )######/\##########|\#_
           |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
           `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
              `   `  `      `   / | |  | | \   '      '  '   '
                               (  | |  | |  )
                              __\ | |  | | /__
                             (vvv(VVV)(VVV)vvv)

    """
    print("\n")
    print(r"""
                        ___====-_  _-====___
                  _--^^^#####//      \\#####^^^--_
               _-^##########// (    ) \\##########^-_
              -############//  |\^^/|  \\############-
            _/############//   (@::@)   \\############\_
           /#############((     \\//     ))#############\
          -###############\\    (oo)    //###############-
         -#################\\  / VV \  //#################-
        -###################\\/      \//###################-
        #/|##########/\######(   /\   )######/\##########|\#_
       |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
       `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
          `   `  `      `   / | |  | | \   '      '  '   '
                           (  | |  | |  )
                          __\ | |  | | /__
                         (vvv(VVV)(VVV)vvv)""")


def print_character(character):
    """Print stylized text showing the user their created character.

    Computational Thinking:
    Algorithms: I used the .keys method to print the character information in a more user friendly way.

    :param character: a fully formed character in dictionary form
    :precondition: character must be a fully formed character in dictionary form
    :postcondition: a correctly printed and stylized version of the specified character

    >>> print_character({'Name': 'ba', 'Class': 'barbarian', 'Race': 'human', 'Inventory': [], 'Experience': 0,\
                    'Strength': 14, 'Dexterity': 13, 'Constitution': 6, 'Intelligence': 8, 'Wisdom': 18, 'Charisma': 9,\
                    'HP': [3, 3]})
    <=+=+=+=+=+=+=+=+=>
    Name ba
    Class barbarian
    Race human
    Inventory []
    Experience 0
    Strength 14
    Dexterity 13
    Constitution 6
    Intelligence 8
    Wisdom 18
    Charisma 9
    HP [3, 3]
    <=+=+=+=+=+=+=+=+=>
    """
    print("<=+=+=+=+=+=+=+=+=>")
    for key in character.keys():
        print(key, character[key])
    print("<=+=+=+=+=+=+=+=+=>")


def choose_inventory(character):
    """Prompt user to choose items for their character's inventory.

    Computational Thinking:
    Abstraction: a while loop with nested if statements was used to allow for different scenarios.  First, if user
        input was within the range of the enumerated item list, then the function would run and the user would
        buy that item.  Second, if the user input was -1, then the loop would break and the user would exit the shop.
        Lastly, if the user input was outside the range of the enumerated item list and not -1, then the user would be
        prompted to enter a new item choice. This enumerate method is also used in select_race and select_class and
         is a good way to present lists in a more user friendly way.
    Algorithms: The enumerate function was used to display the inventory list in a more user-friendly way, as well as
        allow for the user to make a selection by typing in the integer relating to the class instead of having to type
        in the whole class name.

    :param character: a fully formed character in dictionary form
    :precondition: character must be a fully formed character in dictionary form.
    :postcondition: user has chosen which items they wanted to buy, and those items have been added to the character's
        inventory in the character dictionary.
    """
    print("\nIf you want to beat the Dragonlord, first you need some gear. Visit Olgierd's shop.")
    print("\n\nWelcome to Olgierd's!\nHere's what I have for sale:")

    inventory = ["sword", "dagger", "bow", "staff", "potion of fire resistance"]

    while True:
        for i, item in enumerate(inventory, 1):
            print("%d: %s" % (i, item))
        item_number = int(input("Which item would you like to buy? (-1 to finish)"))
        if ((len(inventory) < item_number) or (item_number == 0)) and (item_number != -1):
            print("Your choice must be within the store's availability")
        elif item_number == -1:     # exits the shop
            break
        else:
            item_choice = inventory[item_number - 1]      # modifies the character's inventory with the user's purchases
            character["Inventory"].append(item_choice)


def roll_for_initiative():
    """Roll for who attacks first in a round of combat.

    Computational Thinking:
    Decomposition: The helper function roll_die was used to reduce repeated code.
    Algorithms: I used a while loop to repeat the function if the two initiative rolls are equal.

    :postcondition: Correctly returns True if initiative one is higher than initiative two, else False.
    :return: True if initiative one is higher than initiative two, else False.
    """
    initiative1 = 0
    initiative2 = 0

    while initiative1 == initiative2:   # the function continues until there is no draw.
        initiative1 = roll_die(1, 20)
        initiative2 = roll_die(1, 20)
    if initiative1 > initiative2:
        return True
    else:
        return False


def roll_for_damage(character):
    """Roll to determine damage dealt.

    Computational Thinking:
    Decomposition: I invoked the roll_die helper function to reduce repeated code.
    Pattern Matching: Since damage dealt is tied to a character's hit die, I grouped classes with the same hit die
        together to reduce repeated code.

    :param character: a fully formed character in dictionary form
    :precondition: character must be a fully formed character in dictionary form
    :postcondition: returns a random integer value for damage dealt using the correct hit die, and a correctly printed
        message showing how much damage was dealt
    :return: a random integer value for damage dealt using the correct hit die
    """
    character_for_damage = character
    if character_for_damage["Class"] in {"monk", "bard", "druid", "cleric", "rogue", "warlock"}:
        damage = roll_die(1, 8)
    elif character_for_damage["Class"] in {"fighter", "ranger", "paladin"}:
        damage = roll_die(1, 10)
    elif character_for_damage["Class"] in {"sorcerer", "wizard"}:
        damage = roll_die(1, 6)
    else:
        damage = roll_die(1, 12)
    print(character_for_damage["Name"] + f" dealt {damage} damage!")
    return damage


def roll_to_hit(opponent_one, opponent_two):
    """Roll to hit against defender's dexterity.

    Computational Thinking:
    Decomposition: The roll_die helper function was used to reduce repeated code.
    Pattern Matching:
    Abstraction:
    Algorithms:

    :param opponent_one: a fully formed character in dictionary form
    :param opponent_two: a fully formed character in dictionary form
    :precondition: both opponent_one and opponent_two must be fully formed characters in dictionary form.
    :postcondition: Correctly returns True if the character doing the hit has hit, else returns False if they missed.
        Both scenarios also include printing a relevant message.
    :return: True if the character doing the hit has hit, else returns False if they missed
    """
    character_doing_hit = opponent_one      # assigning parameters to local variables
    character_to_hit = opponent_two
    hit_roll = roll_die(1, 20)

    if hit_roll >= character_to_hit["Dexterity"]:
        print(character_doing_hit["Name"] + " has hit!")
        return True
    else:
        print(character_doing_hit["Name"] + " missed!")
        return False


def combat_round(opponent_one, opponent_two):
    """Simulate one round of combat.

    Computational Thinking:
    Decomposition: The helper function roll_for_initiative was used to determine who the attacker and defender would be.
        Next the roll_to_hit helper function was used to determine if the attacker hit.  If the attacker did hit, the
        roll_for_damage helper function was invoked the determine damage, and if that damage was not lethal, then the
        roll_to_hit helper function was invoked for the defender to retaliate.  If the defender hit, then the
        roll_for_damage function was invoked again to determine how much damage they dealt to the attacker.
    Abstraction: This function uses if/else statements and nested if statements to account for multiple scenarios,
        including opponent_one going first versus opponent two going first, the attacker hitting or missing, the
        defender hitting or missing, the attacker/defender dealing enough damage to kill the defender/attacker, and the
         attacker/defender dealing some damage, but not enough to kill the defender/attacker in which case they
         retaliate.
    Algorithms: This function uses an if/else statement to assign opponent_one and opponent_two to local variables that
        can then sent to helper functions as either the attack or defender depending on who rolled higher initiative.
        It then uses nested if statements to play through a round of combat, allowing for hits, misses, lethal-damage,
        non-lethal damage, and retaliation.

    :param opponent_one: a fully formed character in dictionary form
    :param opponent_two: a fully formed character in dictionary form
    :precondition: both opponent_one and opponent_two must be fully formed characters in dictionary form.
    :postcondition: Useful information about what occured during the combat round has been printed for the user, and if
        the characters were dealt damagae during the combat round, that damage is returned and modifies their current HP
    :return: each character's current HP
    """
    if roll_for_initiative():
        attacker = opponent_one    # assigning the character that rolled higher in roll_for_initiative to the attacker
        defender = opponent_two
        print(f"{attacker['Name']} goes first! ")
    else:
        attacker = opponent_two
        defender = opponent_one
        print(f"{attacker['Name']} goes first! ")

    if roll_to_hit(attacker, defender):     # if the attacker hits, they deal damage to the defender
        defender["HP"][1] = defender["HP"][1] - roll_for_damage(attacker)   # modifying the defender's current HP
        if defender["HP"][1] <= 0:
            print(f"{defender['Name']} has died!")

    if defender["HP"][1] > 0:   # if character who attacks second is still alive, they get a chance to retaliate
        print(f"{defender['Name']} retaliates! ")
        if roll_to_hit(defender, attacker):     # if the defender hits, they deal damage to the attacker
            attacker["HP"][1] = attacker["HP"][1] - roll_for_damage(defender)  # modifying the attacker's current HP
            if attacker["HP"][1] <= 0:
                print(f"{attacker['Name']} has died!")

    return attacker["HP"][1], defender["HP"][1]


def main():
    """Run the functions in this module.
    """
    doctest.testmod()
    print("\nGreetings Traveller!\n")
    number_of_syllables = input("How many syllables is your name?")
    main_character = create_character(number_of_syllables)
    print_dragon()
    print("\nA new challenger approaches, eager to face the Dragonlord!")
    print("Here is your challenger:\n")
    print_character(main_character)
    choose_inventory(main_character)
    print("\n")
    print_character(main_character)
    villain = {'Name': 'miraak', 'Class': 'barbarian', 'Race': 'dragonborn',
               'Inventory': ["Miraak's Staff", "Miraak's Sword"], 'Experience': 100, 'Strength': 12, 'Dexterity': 10,
               'constitution': 10, 'intelligence': 11, 'wisdom': 9, 'charisma': 8,
               'HP': [7, 7]}
    print("\nOh no! One of the Dragonlord's lieutenants has appeared. You must defeat him.\n")
    print_character(villain)
    print("\nThe sounds of combat echo down the halls...\n")
    combat_round(main_character, villain)

    # to loop combat the following code code be used instead of the above line:
    # while True:
    #     i = input("Press enter to begin combat... ")
    #     if not i:
    #         while main_character["HP"][1] > 0 and villain["HP"][1] > 0:
    #               combat_round(main_character, villain)


if __name__ == "__main__":
    main()
