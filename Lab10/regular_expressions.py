import re


def is_email(address: str) -> bool:
    """Check if address is a valid email address.

    :param address: a string
    :precondition: address must be a string
    :postcondition: correctly determines if address is a valid email address

    """
    email_regex = re.compile(r"(^[\w]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$)")
    match_object = email_regex.search(address)
    # if match_object:
    #     return True
    # else:
    #     return False
    return True if match_object else False


def is_nakamoto(name: str) -> bool:
    """Check if name is a two part name with a last name of Nakamoto.

    :param name: a string
    :precondition: name must be a string
    :postcondition: correctly determines if name is a two part name with a last name of Nakamoto
    :return: True if name is a two part name with a last name of Nakamoto, else False
    """
    name_regex = re.compile(r"^([A-Z][a-z]*)+ Nakamoto$")
    match_object = name_regex.search(name)
    # if match_object:
    #     # print(f"the Nakamoto name you entered is {match_object.group()}")
    #     return True
    # else:
    #     # print("that is not a Nakamoto name")
    #     return False
    return True if match_object else False


def is_poker(hand: str) -> bool:
    """Check if hand is a valid poker hand.

    :param hand: a string of five alpha-numeric characters
    :precondition: hand must be a string of five alpha-numeric characters, and duplicate cards are always adjacent
    :postcondition: correctly determines if hand is valid
    :return: True if hand is valid, else False
    """
    card_regex = re.compile(r"^[2-9tjqka]{5}$", re.I)
    match_object = card_regex.search(hand)
    if match_object:
        hand_regex = re.compile(r"^(.)\1{4,}$")
        match_object = hand_regex.search(hand)
        if not match_object:
            return True
        else:
            return False
    else:
        return False


def main():
    address = "duncankeen@gmail.com"
    name = "Henry nakamoto"
    hand = "ajk23"
    is_email(address)
    is_nakamoto(name)
    is_poker(hand)


if __name__ == "__main__":
    main()
