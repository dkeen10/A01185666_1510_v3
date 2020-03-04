import doctest
# def make_board():
#     board = {(0, 0): 1, (0, 1): 2, (0, 2): 3, (0, 3): 4, (0, 4): 5,
#              (1, 0): 6, (1, 1): 7, (1, 2): 8, (1, 3): 9, (1, 4): 10,
#              (2, 0): 11, (2, 1): 12, (2, 2): 13, (2, 3): 14, (2, 4): 15,
#              (3, 0): 16, (3, 1): 17, (3, 2): 18, (3, 3): 19, (3, 4): 20,
#              (4, 0): 21, (4, 1): 22, (4, 2): 23, (4, 3): 24, (4, 4): 25}
#     return board


def make_board():
    """Create the maze board.

    :postcondition: a dictionary containing a 5x5 coordinate maze has been successfully created
    :return: a dictionary containing a 5x5 coordinate maze

    >>> make_board()
    {(0, 0): False, (1, 0): False, (2, 0): False, (3, 0): False, (4, 0): False, (0, 1): False, (1, 1): False, \
(2, 1): False, (3, 1): False, (4, 1): False, (0, 2): False, (1, 2): False, (2, 2): False, (3, 2): False, \
(4, 2): False, (0, 3): False, (1, 3): False, (2, 3): False, (3, 3): False, (4, 3): False, (0, 4): False, \
(1, 4): False, (2, 4): False, (3, 4): False, (4, 4): True}

    """
    # board = {(0, 0): [0, 0], (0, 1): [0, 1], (0, 2): [0, 2], (0, 3): [0, 3], (0, 4): [0, 4],
    #          (1, 0): [1, 0], (1, 1): [1, 1], (1, 2): [1, 2], (1, 3): [1, 3], (1, 4): [1, 4],
    #          (2, 0): [2, 0], (2, 1): [2, 1], (2, 2): [2, 2], (2, 3): [2, 3], (2, 4): [2, 4],
    #          (3, 0): [3, 0], (3, 1): [3, 1], (3, 2): [3, 2], (3, 3): [3, 3], (3, 4): [3, 4],
    #          (4, 0): [4, 0], (4, 1): [4, 1], (4, 2): [4, 2], (4, 3): [4, 3], (4, 4): [4, 4]}
    coordinates = [(i, j) for j in range(5) for i in range(5)]
    k = 0
    board = {}
    while k < len(coordinates):
        board[coordinates[k]] = False
        k += 1
    board[(4, 4)] = True
    return board


def validate_move(board, character, direction):
    """Check if direction is valid

    :param board: a 5x5 coordinate dictionary
    :param character: a dictionary containing a location coordinate
    :param direction: user input
    :precondition: board and character must be well formed dictionaries
    :postcondition: correctly identifies if the direction input is valid
    :return: False if direction is not valid, else True

    >>> test_direction1 = "tuba"
    >>> test_board = {(0, 0): False, (1, 0): False, (2, 0): False, (3, 0): False, (4, 0): False, (0, 1): False, \
(1, 1): False, (2, 1): False, (3, 1): False, (4, 1): False, (0, 2): False, (1, 2): False, (2, 2): False, \
(3, 2): False, (4, 2): False, (0, 3): False, (1, 3): False, (2, 3): False, (3, 3): False, (4, 3): False, \
(0, 4): False, (1, 4): False, (2, 4): False, (3, 4): False, (4, 4): True}
    >>> test_character = {"Location": [0,0]}
    >>> validate_move(test_board, test_character, test_direction1)
    Direction must be N, E, S, or W.
    False
    """
    if direction not in {"N", "E", "S", "W"}:
        print("Direction must be N, E, S, or W.")
        return False
    if direction == "N" and (tuple(map(sum, zip(character["Location"], (-1, 0)))) not in board.keys()):
        print("You are at the northern edge of the maze! Enter a different direction.")
        return False
    if direction == "S" and (tuple(map(sum, zip(character["Location"], (1, 0)))) not in board.keys()):
        print("You are at the southern edge of the maze! Enter a different direction.")
        return False
    if direction == "E" and (tuple(map(sum, zip(character["Location"], (0, 1)))) not in board.keys()):
        print("You are at the eastern edge of the maze! Enter a different direction.")
        return False
    if direction == "W" and (tuple(map(sum, zip(character["Location"], (0, -1)))) not in board.keys()):
        print("You are at the western edge of the maze! Enter a different direction:")
        return False
    else:
        return True


# def validate_move(character, direction):
#     if direction not in {"N", "E", "S", "W"}:
#         print("Direction must be N, E, S, or W:")
#         return False
#     if direction == "N" and character["Location"][0] == 0:
#         print("You are at the northern edge of the maze! Enter a different direction:")
#         return False
#     if direction == "S" and character["Location"][0] == 4:
#         print("You are at the southern edge of the maze! Enter a different direction:")
#         return False
#     if direction == "E" and character["Location"][1] == 4:
#         print("You are at the eastern edge of the maze! Enter a different direction:")
#         return False
#     if direction == "W" and character["Location"][1] == 0:
#         print("You are at the western edge of the maze! Enter a different direction:")
#         return False
#     else:
#         return True


def move_character(direction, character):
    """Move the character.

    :param direction: a direction of either N, S, E, or W
    :param character: a dictionary with a location coordinate
    :precondition: direction must be a valid move (N, S, E, or W and destination is within the board)
    :postcondition: character dictionary has been successfully updated after moving in the specified direction

    >>> test_character = {"Location": [0, 0]}
    >>> test_direction = "S"
    >>> move_character(test_direction, test_character)
    >>> print(test_character)
    {'Location': [1, 0]}

    >>> test_character = {"Location": [0, 0]}
    >>> test_direction = "E"
    >>> move_character(test_direction, test_character)
    >>> print(test_character)
    {'Location': [0, 1]}

    >>> test_character = {"Location": [1, 1]}
    >>> test_direction = "N"
    >>> move_character(test_direction, test_character)
    >>> print(test_character)
    {'Location': [0, 1]}

    >>> test_character = {"Location": [1, 1]}
    >>> test_direction = "W"
    >>> move_character(test_direction, test_character)
    >>> print(test_character)
    {'Location': [1, 0]}
    """
    if direction == "N":
        character["Location"][0] -= 1
    if direction == "S":
        character["Location"][0] += 1
    if direction == "W":
        character["Location"][1] -= 1
    if direction == "E":
        character["Location"][1] += 1


# def move_character(board, direction, character):
#     for key in board.keys():
#         if direction == "N":
#             character["Location"] = board[key][0] + 1
#         if direction == "S":
#             character["Location"][0] += 1
#         if direction == "W":
#             character["Location"][1] -= 1
#         if direction == "E":
#             character["Location"][1] += 1


def game():
    """Play the maze game.

    :postcondition: user has successfully played the maze game
    """
    board = make_board()
    character = {"Location": [0, 0]}
    reached_goal = False
    while not reached_goal:
        print(f"Current Location: {character['Location']}")
        direction = input("Move N, S, E, or W?")
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(direction, character)
            if board[tuple(character["Location"])]:
                print("Congratulations! You've reached the end of the maze!")
                reached_goal = True


def main():
    doctest.testmod()
    print("Welcome to the maze! \nYou must reach the bottom right corner.\n")
    game()


if __name__ == "__main__":
    main()
