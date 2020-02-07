"""
Functions to complete the Sieve of Eratosthenes and the least number of bills needed to represent an amount.
Duncan Keen
A01185666
"""
import doctest


def eratosthenes(upper_bound):
    """Calculate all prime numbers that are between zero and an upper bound.

    :param upper_bound: a positive integer
    :precondition: upper_bound must be a positive integer.
    :postcondition: correctly calculates all prime numbers between zero and the upper bound
    :return: a list of prime numbers between zero and an upper bound

    >>> eratosthenes(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    >>> eratosthenes(31)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
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

    >>> cash_money(188.41)
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    >>> cash_money(100.57)
    [1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 2]
    >>> cash_money(10.27)
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2]
    >>> cash_money(1.05)
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
    >>> cash_money(0.02)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
    >>> cash_money(0)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    bills = [
        (100*100, 1),
        (50*100, 1),
        (20*100, 1),
        (10*100, 1),
        (5*100, 1),
        (2*100, 1),
        (1*100, 1),
        (0.25*100, 1),
        (0.1*100, 1),
        (0.05*100, 1),
        (0.01*100, 1)
    ]
    cdn_100 = cdn*100      # I am multiplying all the values by 100 to avoid rounding errors.
    number_of_bills = []
    for (value, bill) in bills:
        (factor, cdn_100) = divmod(cdn_100, value)
        number_of_each = int(bill*factor)
        number_of_bills.append(number_of_each)
    return number_of_bills


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
