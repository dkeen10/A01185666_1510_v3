"""
finally got it to work!
"""

destination_base = int(input("what base between 2 and 9 do you want to convert to?"))
max_number = destination_base ** 4 - 1
print("max number is " + str(max_number))
decimal_number = int(input("enter a base 10 number between 0 and the max number to be converted:"))


def destination_base_input(destination_base):
    """
    asks for destination base
    :return: given destination base
    """
    if 2 <= destination_base <= 9:
        return destination_base
    else:
        print("invalid input")


def decimal_number_input(decimal_number, destination_base, max_number):
    """
    asks for decimal number to be converted
    :return: decimal number
    """
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

    converted_number = str(remainder_1)+str(remainder_2)+str(remainder_3)+str(remainder_4)
    return converted_number


def main(destination_base, max_number, decimal_number):
    """
    asks user for input decimal number and base to which to convert
    :return: converted number in given base
    """
    if 2 <= destination_base <= 9:
        if 0 <= decimal_number <= max_number:
            converted_number = base_conversion(destination_base, decimal_number)
            print(f"the converted number is: {converted_number}")
        else:
            print("invalid input for base 10 number")
    else:
        print("invalid input for destination base")


if __name__ == "__main__":
    main(destination_base, max_number, decimal_number)
