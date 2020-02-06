"""
Duncan Keen
Anunay Ghamal
"""
import doctest


def statistics(number_list):
    """Calculate the a list's length, min value, max value, average, and spread.

    :param number_list: a list of numbers (integers or floats)
    :precondition: must be empty list or a list of numbers
    :postcondition: correctly calculates list length, min value, max value, average, and spread
    :return: a list of the parameter's list length, min value, max value, average, and spread

    >>> statistics([])
    [None, None, None, None, None]
    >>> statistics([1])
    [1, 1, 1, 1.0, 0]
    >>> statistics([0])
    [1, 0, 0, 0.0, 0]
    >>> statistics([0, 0, 0, 0])
    [4, 0, 0, 0.0, 0]
    >>> statistics([1, 2, 3, 4, 5])
    [5, 1, 5, 3.0, 4]
    >>> statistics([-0.5, 0.5])
    [2, -0.5, 0.5, 0.0, 1.0]
    >>> statistics([-1.00, 0, 1])
    [3, -1.0, 1, 0.0, 2.0]
    >>> statistics([0, 0, 1.0])
    [3, 0, 1.0, 0.3333333333333333, 1.0]
    """
    if not number_list:
        return [None, None, None, None, None]

    else:
        list_length = len(number_list)
        min_number = min(number_list)
        max_number = max(number_list)
        sum_of_list = 0

        for i in number_list:
            sum_of_list = sum_of_list + i

        average_of_list = sum_of_list / list_length
        spread = max_number - min_number

        return [list_length, min_number, max_number, average_of_list, spread]


def main():
    #statistics([])
    doctest.testmod()


if __name__ == "__main__":
    main()
