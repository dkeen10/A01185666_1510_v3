"""
this file is an interim version, refer to base_conversion_v3.py for marking
"""


def destination_base_input():
    """
    asks for destination base
    :return: given destination base
    """
    destination_base = int(input("what base between 2 and 9 do you want to convert to?"))
    if 2 <= destination_base <= 9:
        return destination_base
    else:
        print("invalid input")


def max_number_value(destination_base):
    """
    calculates max decimal number for a 4 digit number of given base
    :param destination_base: given destination base
    :return: max allowable decimal number
    """
    max_number = destination_base ** 4 - 1
    print("max number is " + str(max_number))
    return max_number


def decimal_number_input(max_number, destination_base):
    """
    asks for decimal number to be converted
    :return: decimal number
    """
    decimal_number = int(input("enter a base 10 number between 0 and the max number to be converted:"))
    max_number_value()
    if 0 <= decimal_number <= int(max_number):
        print(f"the converted number is: {base_conversion(destination_base, decimal_number)}")
    else:
        print("invalid input")
    return decimal_number


def base_conversion(destination_base, decimal_number):
    """
    calculates converted number in given base
    :param destination_base: destination base to use for conversion
    :param decimal_number: decimal number to be converted
    :return: converted number in given base
    """
    remainder_4 = decimal_number % destination_base
    remainder_3 = (decimal_number // destination_base) % destination_base
    remainder_2 = (decimal_number // destination_base // destination_base) % destination_base
    remainder_1 = (decimal_number // destination_base // destination_base // destination_base) % destination_base
    return str(remainder_1)+str(remainder_2)+str(remainder_3)+str(remainder_4)


def main(destination_base, max_number, decimal_number):
    """
    asks user for input decimal number and base to which to convert
    :return: converted number in given base
    """
    destination_base = destination_base_input()
    if 2 <= destination_base <= 9:
        max_number_value(destination_base)
        decimal_number_input(destination_base, max_number)
        if 0 <= decimal_number_input(destination_base, max_number) <= int(max_number_value(destination_base)):
            print(f"the converted number is: {base_conversion(destination_base, decimal_number)}")
        else:
            print("invalid input")
    else:
        print("invalid input")


if __name__ == "__main__":
    main(destination_base, max)
