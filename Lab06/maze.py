import doctest


def make_board(size: int) -> dict:
    """Create the maze board.

    :param size: a positive, non-zero integer
    :precondition: size must be a positive, non-zero integer
    :postcondition: a dictionary containing a 5x5 coordinate maze has been successfully created
    :return: a dictionary containing a 5x5 coordinate maze
    >>> test_size = 1
    >>> make_board(test_size)
    {(0, 0): True}
    >>> test_size = 5
    >>> make_board(test_size)
    {(0, 0): False, (1, 0): False, (2, 0): False, (3, 0): False, (4, 0): False, (0, 1): False, (1, 1): False, \
(2, 1): False, (3, 1): False, (4, 1): False, (0, 2): False, (1, 2): False, (2, 2): False, (3, 2): False, \
(4, 2): False, (0, 3): False, (1, 3): False, (2, 3): False, (3, 3): False, (4, 3): False, (0, 4): False, \
(1, 4): False, (2, 4): False, (3, 4): False, (4, 4): True}
    """
    coordinates = [(i, j) for j in range(size) for i in range(size)]
    k = 0
    board = {}
    while k < len(coordinates):
        board[coordinates[k]] = False
        k += 1
    board[(size - 1, size - 1)] = True
    return board


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """Check if direction is valid.

    :param board: a 5x5 coordinate dictionary
    :param character: a dictionary containing a location coordinate
    :param direction: a string
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
    >>> test_direction1 = "N"
    >>> test_board = {(0, 0): False, (1, 0): False, (2, 0): False, (3, 0): False, (4, 0): False, (0, 1): False, \
(1, 1): False, (2, 1): False, (3, 1): False, (4, 1): False, (0, 2): False, (1, 2): False, (2, 2): False, \
(3, 2): False, (4, 2): False, (0, 3): False, (1, 3): False, (2, 3): False, (3, 3): False, (4, 3): False, \
(0, 4): False, (1, 4): False, (2, 4): False, (3, 4): False, (4, 4): True}
    >>> test_character = {"Location": [0,0]}
    >>> validate_move(test_board, test_character, test_direction1)
    You are at the northern edge of the maze! Enter a different direction.
    False
    >>> test_direction1 = "S"
    >>> test_board = {(0, 0): False, (1, 0): False, (2, 0): False, (3, 0): False, (4, 0): False, (0, 1): False, \
(1, 1): False, (2, 1): False, (3, 1): False, (4, 1): False, (0, 2): False, (1, 2): False, (2, 2): False, \
(3, 2): False, (4, 2): False, (0, 3): False, (1, 3): False, (2, 3): False, (3, 3): False, (4, 3): False, \
(0, 4): False, (1, 4): False, (2, 4): False, (3, 4): False, (4, 4): True}
    >>> test_character = {"Location": [4,0]}
    >>> validate_move(test_board, test_character, test_direction1)
    You are at the southern edge of the maze! Enter a different direction.
    False
    >>> test_direction1 = "E"
    >>> test_board = {(0, 0): False, (1, 0): False, (2, 0): False, (3, 0): False, (4, 0): False, (0, 1): False, \
(1, 1): False, (2, 1): False, (3, 1): False, (4, 1): False, (0, 2): False, (1, 2): False, (2, 2): False, \
(3, 2): False, (4, 2): False, (0, 3): False, (1, 3): False, (2, 3): False, (3, 3): False, (4, 3): False, \
(0, 4): False, (1, 4): False, (2, 4): False, (3, 4): False, (4, 4): True}
    >>> test_character = {"Location": [0,4]}
    >>> validate_move(test_board, test_character, test_direction1)
    You are at the eastern edge of the maze! Enter a different direction.
    False
    >>> test_direction1 = "W"
    >>> test_board = {(0, 0): False, (1, 0): False, (2, 0): False, (3, 0): False, (4, 0): False, (0, 1): False, \
(1, 1): False, (2, 1): False, (3, 1): False, (4, 1): False, (0, 2): False, (1, 2): False, (2, 2): False, \
(3, 2): False, (4, 2): False, (0, 3): False, (1, 3): False, (2, 3): False, (3, 3): False, (4, 3): False, \
(0, 4): False, (1, 4): False, (2, 4): False, (3, 4): False, (4, 4): True}
    >>> test_character = {"Location": [0,0]}
    >>> validate_move(test_board, test_character, test_direction1)
    You are at the western edge of the maze! Enter a different direction.
    False
    >>> test_direction1 = "E"
    >>> test_board = {(0, 0): False, (1, 0): False, (2, 0): False, (3, 0): False, (4, 0): False, (0, 1): False, \
(1, 1): False, (2, 1): False, (3, 1): False, (4, 1): False, (0, 2): False, (1, 2): False, (2, 2): False, \
(3, 2): False, (4, 2): False, (0, 3): False, (1, 3): False, (2, 3): False, (3, 3): False, (4, 3): False, \
(0, 4): False, (1, 4): False, (2, 4): False, (3, 4): False, (4, 4): True}
    >>> test_character = {"Location": [0,0]}
    >>> validate_move(test_board, test_character, test_direction1)
    True
    """
    if direction not in {"N", "E", "S", "W"}:
        print("Direction must be N, E, S, or W.")
        return False
    # the below is taking the character's location and moving it in the indicated direction, then checking if the result
    # is in the coordinate dictionary:
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
        print("You are at the western edge of the maze! Enter a different direction.")
        return False
    else:
        return True


def move_character(direction: str, character: dict):
    """Move the character.

    :param direction: a string indicating a direction of either N, S, E, or W
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


def game():
    """Play the maze game.

    :postcondition: user has successfully played the maze game
    """
    size = 5
    board = make_board(size)
    character = {"Location": [0, 0]}
    reached_goal = False
    while not reached_goal:
        print(f"Current Location: {character['Location']}")
        direction = input("Move N, S, E, or W?")
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(direction, character)
            if board[tuple(character["Location"])]:
                print(f"Current Location: {character['Location']}")
                print("Congratulations! You've reached the end of the maze!")
                reached_goal = True


def main():
    doctest.testmod()
    print("Welcome to the maze! \nYou must reach the bottom right corner.\n")
    game()


if __name__ == "__main__":
    main()
