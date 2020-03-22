import ao3


def attack(attacker: dict, defender: dict):
    """Fight a round a of combat.

    :param attacker: dictionary of attacker
    :param defender: dictionary of defender
    :precondition: must give dictionaries of attacker and defender with name and HP
    :postcondition: attacker and defender engage in a round of combat.
    """
    if ao3.roll_die(1, 2) == 2:
        damage = ao3.roll_die(1, 6)
        defender['HP'] = defender['HP'] - damage
        print(attacker['Name'] + " lands a hit!\n" + defender["Name"] +
              " cries out in pain, they have lost " + str(damage) + " hitpoints.")
        if defender['HP'] <= 0:
            print(defender['Name'] + " has died...")
    else:
        print(attacker['Name'] + ' misses wildly!')


def combat_to_death(first_attacker: dict, second_attacker: dict):
    """Fight two combatants until death.

    :param first_attacker: dictionary of first attacker
    :param second_attacker: dictionary of second attacker
    :precondition: must give dictionaries of first and second attackers containing HP and Names
    :postcondition: the attackers fight until death
    """
    print(first_attacker['Name'] + ' is the first to make a move...')
    while first_attacker['HP'] > 0 and second_attacker['HP'] > 0:
        attack(first_attacker, second_attacker)
        if first_attacker['HP'] > 0 and second_attacker['HP'] > 0:
            attack(second_attacker, first_attacker)


def initiate_combat(opponent_one: dict, opponent_two: dict):
    """Initiate combat between two combatants.

    :param opponent_one: A dictionary for a character
    :param opponent_two: A dictionary for a character
    :precondition: give two dictionaries for two characters
    :postcondition: The order of attack is determined
    """
    print("\n" + opponent_one['Name'] + ' and the ' + opponent_two['Name'] + ' face each other in combat.\n')
    opponent_one_initiative = 0
    opponent_two_initiative = 0
    while opponent_one_initiative == opponent_two_initiative:
        opponent_one_initiative = ao3.roll_die(1, 20)
        opponent_two_initiative = ao3.roll_die(1, 20)
    if opponent_one_initiative > opponent_two_initiative:
        combat_to_death(opponent_one, opponent_two)
    else:
        combat_to_death(opponent_two, opponent_one)


if __name__ == "__main__":
    you = {'Name': 'player', 'HP': 10, 'Location': (3, 3)}
    foe = {'Name': 'Goblin', 'HP': 5}

    initiate_combat(you, foe)
