# def make_board():
#     board = {(0, 0): 1, (0, 1): 2, (0, 2): 3, (0, 3): 4, (0, 4): 5,
#              (1, 0): 6, (1, 1): 7, (1, 2): 8, (1, 3): 9, (1, 4): 10,
#              (2, 0): 11, (2, 1): 12, (2, 2): 13, (2, 3): 14, (2, 4): 15,
#              (3, 0): 16, (3, 1): 17, (3, 2): 18, (3, 3): 19, (3, 4): 20,
#              (4, 0): 21, (4, 1): 22, (4, 2): 23, (4, 3): 24, (4, 4): 25}
#     return board


def make_board():
    board = {(0, 0): [0, 0], (0, 1): [0, 1], (0, 2): [0, 2], (0, 3): [0, 3], (0, 4): [0, 4],
             (1, 0): [1, 0], (1, 1): [1, 1], (1, 2): [1, 2], (1, 3): [1, 3], (1, 4): [1, 4],
             (2, 0): [2, 0], (2, 1): [2, 1], (2, 2): [2, 2], (2, 3): [2, 3], (2, 4): [2, 4],
             (3, 0): [3, 0], (3, 1): [3, 1], (3, 2): [3, 2], (3, 3): [3, 3], (3, 4): [3, 4],
             (4, 0): [4, 0], (4, 1): [4, 1], (4, 2): [4, 2], (4, 3): [4, 3], (4, 4): [4, 4]}
    return board


def validate_move(character, direction):
    if direction not in {"N", "E", "S", "W"}:
        print("Direction must be N, E, S, or W:")
        return False
    if direction == "N" and character["Location"][0] == 0:
        print("You are at the northern edge of the maze! Enter a different direction:")
        return False
    if direction == "S" and character["Location"][0] == 4:
        print("You are at the southern edge of the maze! Enter a different direction:")
        return False
    if direction == "E" and character["Location"][1] == 4:
        print("You are at the eastern edge of the maze! Enter a different direction:")
        return False
    if direction == "W" and character["Location"][1] == 0:
        print("You are at the western edge of the maze! Enter a different direction:")
        return False
    else:
        return True


def move_character(direction, character):
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
    # board = make_board()
    character = {"Location": [0, 0]}
    reached_goal = False
    while not reached_goal:
        print(f"Current Location: {character['Location']}")
        direction = input("Move N, S, E, or W?")
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(direction, character)
            if character["Location"] == [4, 4]:
                print("Congratulations! You've Reached the end of the maze!")
                reached_goal = True


def main():
    print("Welcome to the maze! \nYou must reach the bottom right corner.\n")
    game()


if __name__ == "__main__":
    main()
