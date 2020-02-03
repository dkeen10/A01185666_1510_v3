# def main():
#     format_name = (str.title(input("what is your first name?") + " " +
#         str.title(input("what is your last name?"))))
#     print(format_name)
#
#     tripler = input("what do you want tripled?")
#     print(str(tripler)+str(tripler)+str(tripler))
#
#     print("(9+9)(99/9+999) is equal to:")
#     this_year = int((9 + 9)*(99/9 + 999)/9)
#     print(this_year)
#
#     base_conversion = int(input("what base between 2 and 9 do you want to convert to?"))
#     max_number = base_conversion ** 4 - 1
#     print("max number is", max_number)
#     decimal_number = int(
#         input("enter a base 10 number between 0 the max number to convert to the designated base number:"))
#     remainder_4 = decimal_number % base_conversion
#     remainder_3 = (decimal_number // base_conversion) % base_conversion
#     remainder_2 = (decimal_number // base_conversion // base_conversion) % base_conversion
#     remainder_1 = (decimal_number // base_conversion // base_conversion // base_conversion) % base_conversion
#
#     print("the converted number is:" + str(remainder_1) + str(remainder_2) + str(remainder_3) + str(remainder_4))
#
#
# if __name__ == "__main__":
#     main()


def format_name():
    full_name = (str.strip(str.title(input("what is your first name?"))) + " " +
        str.strip(str.title(input("what is your last name?"))))
    print(full_name)


def tripler():
    tripling = input("what do you want tripled?")
    print(str(tripling)+str(tripling)+str(tripling))


def this_year():
    print("(9+9)(99/9+999) is equal to:")
    twenty_twenty = int((9 + 9)*(99/9 + 999)/9)
    print(twenty_twenty)


def base_conversion():

    destination_base = int(input("what base between 2 and 9 do you want to convert to?"))
    if 2 <= destination_base <= 9:
        max_number = destination_base ** 4 - 1
        print("max number is", max_number)
        decimal_number = int(
            input("enter a base 10 number between 0 the max number to convert to the designated base number:"))
        if 0 <= decimal_number <= int(max_number):
            remainder_4 = decimal_number % destination_base
            remainder_3 = (decimal_number // destination_base) % destination_base
            remainder_2 = (decimal_number // destination_base // destination_base) % destination_base
            remainder_1 = (decimal_number // destination_base // destination_base // destination_base) % destination_base

            print(
                "the converted number is:" + str(remainder_1) + str(remainder_2) + str(remainder_3) + str(remainder_4))
        else:
            print("invalid input")
    else:
        print("invalid input")


def main():
    format_name()
    tripler()
    this_year()
    base_conversion()


if __name__ == "__main__":
    main()



# answer = input("do you want run functions.py again? (yes/no)")
# if answer == "yes":
#     format_name_2 = (str.title(input("what is your first name?") + " " +
#         str.title(input("what is your last name?"))))
#     print(format_name_2)
#
#     tripler_2 = input("what do you want tripled?")
#     print(str(tripler_2) + str(tripler_2) + str(tripler_2))
#
#     print("(9+9)(99/9+999) is equal to:")
#     this_year_2 = int((9 + 9) * (99 / 9 + 999) / 9)
#     print(this_year_2)
# elif answer == "no":
#     print("ok")
# else:
#     print("invalid input")

# all the functions in functions.py should work with any input. For format_name, it converts
# any input into a string.  The tripler function works the same.  For the if statement in part d,
# it has options for all input types.
    

