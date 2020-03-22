import math


def heron(number: int) -> float:
    """
    :param number: a positive integer
    :precondition: number must be a positive integer
    :postcondition: successfully finds the square root of the number to within 2 decimal places.
    :raise zeroDivisionError:
    :return: the square root of the number within 2 decimal places

    """
    guess = abs(number)
    while not math.isclose(guess ** 2, number, abs_tol=0.001):
        try:
            guess = (guess + number / guess) / 2
        except ZeroDivisionError:
            print("guess can't be zero!")
            return -1
    print(guess)
    return guess


def find_an_even(input_list: list) -> int:
    """Return the first even number in input_list

    :param input_list: a list of integers
    :precondition: input_list must be a list of integer
    :postcondition: return the first even number in input_list
    :raise ValueError: if input_list does not contain an even number
    :return: first even number in input_list
    """
    for i in input_list:
        if i % 2 == 0:
            print(i)
            return i
        raise ValueError ("There were no evens")


def main():
    try:
        heron(42)
    except TypeError:
        print("input must be an integer!")

    find_an_even([1, 2, 3])


if __name__ == "__main__":
    main()
