# base_conversion = int(input("what base between 2 and 9 do you want to convert to?"))
# max_number = base_conversion ** 4 - 1
# print("max number is", max_number)
# decimal_number = int(
#     input("enter a base 10 number between 0 and the max number to convert to the designated base number:"))
#
# remainder_4 = decimal_number % base_conversion
# remainder_3 = (decimal_number // base_conversion) % base_conversion
# remainder_2 = (decimal_number // base_conversion // base_conversion) % base_conversion
# remainder_1 = (decimal_number // base_conversion // base_conversion // base_conversion) % base_conversion
#
# print("the converted number is:" + str(remainder_1) + str(remainder_2) + str(remainder_3) + str(remainder_4))





base_conversion = int(input("what base between 2 and 9 do you want to convert to?"))
if 2 <= base_conversion <=9:
    max_number = base_conversion ** 4 - 1
    print("max number is", max_number)
    decimal_number = int(input("enter a base 10 number between 0 the max number to convert to the designated base number:"))
    if 0 <= decimal_number <= int(max_number):
        remainder_4 = decimal_number % base_conversion
        remainder_3 = (decimal_number // base_conversion) % base_conversion
        remainder_2 = (decimal_number // base_conversion // base_conversion) % base_conversion
        remainder_1 = (decimal_number // base_conversion // base_conversion // base_conversion) % base_conversion


        print("the converted number is:" + str(remainder_1) + str(remainder_2) + str(remainder_3) + str(remainder_4))
    else:
        print("invalid input")
else:
    print("invalid input")

# number_to_convert = input(float("enter a base 10 number between 0 and 6560 to convert into a 4 digit number:"))
# base = input("what base between 2 and 9 do you want it converted to?")
# if basenumber_to_convert > 6560:
#     print("sorry that number is too large")
# elif 6560 >= number_to_convert > 4095:
#
# elif 4095 >= number_to_convert > 2400:
# elif 2400 >= number_to_convert > 1295:
# elif 1295 >= number_to_convert > 624:
# elif 624 >= number_to_convert > 255:
# elif 255 >= number_to_convert > 80:
# elif 80 >= number_to_convert > 15:
# elif 15 >= number_to_convert >= 0:
# elif number_to_convert < 0:
#     print ("sorry that number is too small")
# else:
#    print ("invalid input)