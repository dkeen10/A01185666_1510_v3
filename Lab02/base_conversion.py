"""
this file works, but is not fully functionally decomposed.  refer to base_conversion_v3.py for marking.
"""

def base_conversion():
    """
    converts decimal number input into 4 digit number of given base
    :return: 4 digit number in given base
    """
    destination_base = int(input("what base between 2 and 9 do you want to convert to?"))

    if 2 <= destination_base <= 9:
        max_number = destination_base ** 4 - 1
        print("max number is", max_number)
        decimal_number = int(
            input("enter a base 10 number between 0 the max number to convert to the designated base number:"))

        if 0 <= decimal_number <= int(max_number):
            print(
                "the converted number is:" + str(base_conversion_calc(decimal_number, destination_base)))
        else:
            print("invalid input")
    else:
        print("invalid input")


def base_conversion_calc(decimal_number, destination_base):
    """
    converts decimal number input into 4 digit number of given base
    :param decimal_number: base 10 number input
    :param destination_base: given base
    :return: 4 digit number in given base
    """
    remainder_4 = decimal_number % destination_base
    remainder_3 = (decimal_number // destination_base) % destination_base
    remainder_2 = (decimal_number // destination_base // destination_base) % destination_base
    remainder_1 = (decimal_number // destination_base // destination_base // destination_base) % destination_base
    return str(remainder_1) + str(remainder_2) + str(remainder_3) + str(remainder_4)


if __name__ == "__main__":
    base_conversion()
