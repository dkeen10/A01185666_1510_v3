import doctest
import math


def heron(number: int) -> float:
    """Find the square root of the specified integer.

    :param number: an integer
    :precondition: number must be an integer
    :postcondition: successfully finds the square root of the number to within 2 decimal places.
    :raise zeroDivisionError: if number is a negative integer
    :return: the square root of the number within 2 decimal places

    >>> heron(97)
    9.85
    >>> heron(0)
    0
    >>> heron (9)
    3.0
    """
    guess = number
    while not math.isclose(guess ** 2, number, abs_tol=0.000001):
        try:
            if guess <= -1:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("I can't do that!")
            return -1
        else:
            guess = (guess + number / guess) / 2
    return round(guess, 2)


def find_an_even(input_list: list) -> int:
    """Return the first even number in input_list.

    :param input_list: a list of integers
    :precondition: input_list must be a list of integer
    :postcondition: return the first even number in input_list
    :raise ValueError: if input_list does not contain an even number
    :return: first even number in input_list

    >>> find_an_even([0])
    0
    >>> find_an_even([1, 2, 3])
    2
    """
    for i in input_list:
        if i % 2 == 0:
            return i
    raise ValueError("There were no evens input list")


def main():
    doctest.testmod()
    try:
        heron(97)
    except TypeError:
        print("input must be an integer!")
    find_an_even([0])


if __name__ == "__main__":
    main()
