import re
import doctest


def is_email(address: str) -> bool:
    """Check if address is a valid email address.

    :param address: a string
    :precondition: address must be a string
    :postcondition: correctly determines if address is a valid email address
    :return: True if email is valid, else False

    >>> is_email("duncankeen@gmail.com")
    True
    >>> is_email("duncan_keen@gmail.com")
    True
    >>> is_email("duncankeen@hotmail.ca")
    True
    >>> is_email("duncan$keen@gmail.com")
    False
    >>> is_email("duncankeen@.com")
    False
    >>> is_email("@gmail.com")
    False
    >>> is_email("duncankeen@gmail.com.com")
    False
    >>> is_email("duncankeen@gmail.c")
    False
    >>> is_email("duncankeen@gmailcom")
    False
    >>> is_email("duncankeengmail.com")
    False
    """
    email_regex = re.compile(r"(^[\w]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]{2,4}$)")
    match_object = email_regex.search(address)
    return True if match_object else False


def is_nakamoto(name: str) -> bool:
    """Check if name is a two part name with a last name of Nakamoto.

    :param name: a string
    :precondition: name must be a string
    :postcondition: correctly determines if name is a two part name with a last name of Nakamoto
    :return: True if name is a two part name with a last name of Nakamoto, else False

i. ‘Satoshi Nakamoto’ ii. ‘Alice Nakamoto’ iii. ‘Robocop Nakamoto
    >>> is_nakamoto("Satoshi Nakamoto")
    True
    >>> is_nakamoto("Alice Nakamoto")
    True
    >>> is_nakamoto("Robocop Nakamoto")
    True
    >>> is_nakamoto("Satoshi nakamoto")
    False
    >>> is_nakamoto("satoshi Nakamoto")
    False
    >>> is_nakamoto("Nakamoto")
    False
    >>> is_nakamoto("Mr. Nakamoto")
    False
    """
    name_regex = re.compile(r"^([A-Z][a-z]*)+ Nakamoto$")
    match_object = name_regex.search(name)
    return True if match_object else False


def is_poker(hand: str) -> bool:
    """Check if hand is a valid poker hand.

    :param hand: a string of five alpha-numeric characters
    :precondition: hand must be a string of five alpha-numeric characters, and duplicate cards are always adjacent
    :postcondition: correctly determines if hand is valid
    :return: True if hand is valid, else False

    >>> is_poker("aaaak")
    True
    >>> is_poker("aAaAK")
    True
    >>> is_poker("aaakk")
    True
    >>> is_poker("aakk2")
    True
    >>> is_poker("aa342")
    True
    >>> is_poker("23456")
    True
    >>> is_poker("aaaa1")
    False
    >>> is_poker("aaaaa")
    False
    >>> is_poker("aa")
    False
    >>> is_poker("aa2233")
    False
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
    doctest.testmod()
    address = "duncankeen@gmail.com"
    name = "Henry nakamoto"
    hand = "ajk23"
    is_email(address)
    is_nakamoto(name)
    is_poker(hand)


if __name__ == "__main__":
    main()
