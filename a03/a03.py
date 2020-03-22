import random
import Combat
import character
import doctest


def quit_game():
    print("\nGAME OVER \nThank you for playing.")


def clean_input(user_string: str) -> str:
    """Clean string of user input.

    :param user_string: user input string
    :precondition: user_string must be a string
    :postcondition: string is removed of whitespace and upper-cased
    :return: a string that has been stripped of whitespace and changed to uppercase

    >>> clean_input('hello')
    'HELLO'
    >>> clean_input(' hello ')
    'HELLO'
    >>> clean_input('h   ')
    'H'
    """
    cleaned_input = user_string.strip()
    return cleaned_input.upper()


def roll_die(number_of_rolls: int, number_of_sides: int) -> int:
    """Roll a die with the specified number of sides the specified number of times.

    :param number_of_rolls: a positive non-zero integer
    :param number_of_sides: a positive non-zero integer
    :precondition: number_of_rolls and number_of_sides must be positive non-zero integers
    :postcondition: generates a random dice role of the correct sided die being rolled the correct number of times
    :return: a correctly generated sum of the dice roll as an integer
    """
    dice_roll = 0
    for i in range(0, number_of_rolls):
        dice_roll += random.randint(1, number_of_sides)
    return dice_roll


def print_map(map_of_dungeon: dict, player: dict, dungeon_width: int):
    """Print out map of player location.

    :param map_of_dungeon: dictionary representing map of dungeon with tuple and string key value pairs
    :param player: dictionary containing character location and hp
    :param dungeon_width: positive int of dungeon width
    :precondition: must give non empty dictionaries of map and player, positive int for dungeon width
    :postcondition: correctly prints out the map with character location and hp of character
    """
    print("Map (you are the X):")
    for coordinate in map_of_dungeon.keys():
        if tuple(player["Location"]) == coordinate:
            print("[X]",  end='')
        else:
            print("[ ]", end='')
        if coordinate[1] == dungeon_width - 1:
            print("")
    print("HP: %d" % player["HP"])


def dungeon_map(map_size: int) -> dict:
    """Generate a map of the dungeon.

    :param map_size: a positive, non-zero number
    :precondition: map_size must be a positive, non-zero number
    :postcondition: a dungeon map has been created and populated
    :return: a dictionary containing a coordinate map of the dungeon as tuple and string pair
    """
    rooms = ["You enter a throne room", "You enter an empty room with a chest", "You enter a dark hallway",
             "You enter a library", "You enter a Trophy Hall", "You enter a vault filled with gold",
             "You enter a storage room", "You enter a Bedchamber"]

    coordinates = [(j, i) for j in range(map_size) for i in range(map_size)]
    k = 0
    dungeon = {}
    while k < len(coordinates):
        dungeon[coordinates[k]] = rooms[roll_die(1, 8) - 1]
        k += 1
    return dungeon


def movement_input(player: dict, dungeon: dict) -> str:
    """Get character movement choice from player.

    :param player: dictionary of player containing location
    :param dungeon: a coordinate map dictionary
    :precondition: must give dictionary containing player location in a list
    :postcondition: correctly determines the player's choice of valid direction as a string
    :return: a string containing the player's valid direction choice
    """
    direction = clean_input(input("Move N, E, S, or W? ('quit' to exit):"))
    continue_looping = True
    while continue_looping:
        if direction not in {"N", "E", "S", "W", "QUIT"}:
            direction = clean_input(input("Direction must be N, E, S, or W:"))
        elif direction == "N" and tuple(map(sum, zip(player["Location"], (-1, 0)))) not in dungeon.keys():
            direction = clean_input(input("You are at the northern edge of the map! Enter a different direction:"))
        elif direction == "S" and tuple(map(sum, zip(player["Location"], (1, 0)))) not in dungeon.keys():
            direction = clean_input(input("You are at the southern edge of the map! Enter a different direction:"))
        elif direction == "E" and tuple(map(sum, zip(player["Location"], (0, 1)))) not in dungeon.keys():
            direction = clean_input(input("You are at the eastern edge of the map! Enter a different direction:"))
        elif direction == "W" and tuple(map(sum, zip(player["Location"], (0, -1)))) not in dungeon.keys():
            direction = clean_input(input("You are at the western edge of the map! Enter a different direction:"))
        elif tuple(player['Location']) in dungeon.keys():
            continue_looping = False
    return direction


def movement(direction: str, player: dict):
    """Move character on the map.

    :param direction: string of player direction
    :param player: dictionary of player containing location
    :precondition: must give string of cardinal direction within the map, dictionary for player containing location
    :postcondition: moves character on the map

    >>> main_character = {'Location': [2, 2]}
    >>> movement('N', main_character)
    >>> main_character
    {'Location': [1, 2]}
    >>> main_character = {'Location': [2, 2]}
    >>> movement('W', main_character)
    >>> main_character
    {'Location': [2, 1]}
    """
    if direction == "N":
        player["Location"][0] -= 1
    if direction == "S":
        player["Location"][0] += 1
    if direction == "W":
        player["Location"][1] -= 1
    if direction == "E":
        player["Location"][1] += 1


def heal_character(player: dict):
    """Heal character for 2 points.

    :param player: dictionary of player containing 'HP'
    :precondition: dictionary of player must have a HP value between 1 and 10
    :postcondition: character's HP value has been correctly increased by 2 points up to a max of 10 HP

    >>> main_character = {'HP': 1}
    >>> heal_character(main_character)
    >>> main_character
    {'HP': 3}
    >>> main_character = {'HP': 10}
    >>> heal_character(main_character)
    >>> main_character
    {'HP': 10}
    """
    if player["HP"] < 10 and player["HP"] != 9:
        player["HP"] += 2
    elif player["HP"] == 9:
        player["HP"] += 1


def flee(player: dict, monster: dict):
    """Let player escape from monster.

    :param player: dictionary of player containing HP
    :param monster: dictionary of monster containing monster name
    :precondition: must give dictionaries of player and monster containing name and HP
    :postcondition: correctly prints that user escaped from combat and if they took damage
    """
    if roll_die(1, 10) == 10:
        damage = roll_die(1, 4)
        player["HP"] -= damage
        print(f"The {monster['Name']} stabbed you in the back for {damage} damage as you fled!")
    else:
        print("you escaped successfully!")


def encounter(player: dict) -> dict:
    """Determine if the player will fight with a monster.

    :param player: dictionary of player containing HP
    :precondition: player must be a correctly formed dictionary
    :postcondition: monster encounter has been correctly handled and if the player survived, heals character's HP
    :return: dictionary of player with updated HP
    """
    if roll_die(1, 4) == 4:
        monster = monster_creation()
        fight_flight = clean_input(input(f"A {monster['Name']} appears! Do you want to fight? (Y/N):"))
        while fight_flight not in {"Y", "N"}:
            fight_flight = clean_input(input("Sorry, your answer must be Y or N:"))
        if fight_flight == "Y":
            Combat.initiate_combat(player, monster)
        else:
            flee(player, monster)
        if player["HP"] <= 0:
            player = death()
    else:
        heal_character(player)
    return player


def death() -> dict:
    """Restart the game on player death.

    :return: dictionary of new player
    """
    print("GAME OVER\n Restarting...")
    player = initialisation()
    return player


def monster_creation() -> dict:
    """Generate a monster.

    :return: Dictionary with monster name and HP
    """
    monster = {"Name": "", "HP": 5}
    monster_names = ["Goblin", "Orc", "Wolf", "Skeleton"]
    monster["Name"] = random.choice(monster_names)
    return monster


def initialisation() -> dict:
    """Start the game with character creation.

    :postcondition: starts game and correctly creates character dictionary
    :return: dictionary of player character
    """
    print("You awake in the middle of a dark and dreary dungeon...")
    syllables = input("How many syllables are in your name?:")
    while not syllables.isnumeric() or int(syllables) < 1:
        syllables = input("Sorry, syllables must be a positive integer:")
    main_character = character.create_character(int(syllables))
    character.print_character(main_character)
    print("You decide to get up and look around.")
    return main_character


def main():
    map_size = 5
    main_character = initialisation()
    dungeon = dungeon_map(map_size)
    direction = None
    while direction != "QUIT":
        print_map(dungeon, main_character, map_size)
        direction = movement_input(main_character, dungeon)
        if direction != 'QUIT':
            movement(direction, main_character)
            print(dungeon[tuple(main_character["Location"])])
            main_character = encounter(main_character)
    quit_game()


if __name__ == "__main__":
    doctest.testmod()
    main()
