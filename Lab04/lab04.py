"""
Functions to complete the Sieve of Eratosthenes and how many bills are needed to represent an amount.
Duncan Keen
A01185666
"""
import doctest


def eratosthenes(number):
    prime_numbers = ""
    return prime_numbers


def cash_money(cdn):
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
        number_of_each = (bill*factor)
        number_of_bills.append(number_of_each)
    print(number_of_bills)
    return number_of_bills


def main():
    doctest.testmod()
    eratosthenes(30)
    cash_money(263.33)


if __name__ == "__main__":
    main()
