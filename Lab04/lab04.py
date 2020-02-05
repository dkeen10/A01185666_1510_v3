"""
Functions to complete the Sieve of Eratosthenes and how many bills are needed to represent an amount.
Duncan Keen
A01185666
"""
import doctest


def eratosthenes(upper_bound):
    """Calculate all prime numbers that are between zero and an upper bound.

    :param upper_bound: a positive integer
    :precondition: upper_bound must be a positive integer.
    :postcondition: correctly calculates all prime numbers between zero and an upper bound
    :return: a list of prime numbers between zero and an upper bound

    >>> eratosthenes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> eratosthenes(0)
    []
    >>> eratosthenes(1)
    []
    >>> eratosthenes(2)
    [2]
    """
    non_prime_numbers = []
    prime_numbers = []

    for i in range(2, upper_bound+1):
        if i not in non_prime_numbers:
            prime_numbers.append(i)
            for j in range(i * i, upper_bound+1, i):
                non_prime_numbers.append(j)
    return prime_numbers


def cash_money(cdn):
    """Convert a dollar value into the least number of bills needed to represent it.

    :param cdn: a positive float of up to two decimal places
    :precondition: cdn must be a positive float of up to two decimal places
    :postcondition: correctly calculates the least number of bills needed
    :return: least number of bills needed to represent the input value, shown in a list

    >>> cash_money(263.33)
    [2, 1, 0, 1, 0, 1, 1, 1, 0, 1, 2]
    >>> cash_money(0.01)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    >>> cash_money(0)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    bills = [
        (100, 1),
        (50, 1),
        (20, 1),
        (10, 1),
        (5, 1),
        (2, 1),
        (1, 1),
        (0.25, 1),
        (0.1, 1),
        (0.05, 1),
        (0.01, 1)
    ]
    number_of_bills = []
    for (value, bill) in bills:
        (factor, cdn) = divmod(cdn, value)
        number_of_each = int(bill*factor)
        number_of_bills.append(number_of_each)
    return number_of_bills


def main():
    doctest.testmod()
    eratosthenes(30)
    cash_money(263.33)


if __name__ == "__main__":
    main()
