"""
Demonstrate how to mock an object.
"""

import random


def roll_die(rolls, sides):
    """
    Roll a die with the specified number of sides the specified number of times.

    :param rolls: a positive non-zero int
    :param sides: a positive non-zero int
    :return: the total roll
    """
    return random.randint(rolls, sides * rolls)
