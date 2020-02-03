"""
Functions to complete seven simple tasks.
Duncan Keen
A01185666
"""
import doctest
import random


def convert_to_roman_numeral(number):
    """Convert decimal numbers to their roman numeral equivalent and returns the result.

    Computational thinking:
    Decomposition: In order to simplify this function, I made a dictionary of roman numerals and their decimal number
        equivalents. I then built a string of roman numerals using the divmod function to combine the floor division and
         modulus steps in the calculation.
    Pattern Matching: I saw that to convert a decimal number into its roman numeral equivalent, the divmod function
        could be used as a shortcut.
    Abstraction: to make this function more ubiquitous, use a dictionary for roman numerals and their decimal
        number equivalents, then use the divmod function to build a new string using the converted numbers.
    Automating with Algorithms: I set the roman_number as an empty string, then used a for loop to build up the
        converted roman numeral.

    :param number: decimal number to be converted
    :precondition: number must be a positive non-zero integer
    :postcondition: calculates the correct roman numeral equivalent
    :return: roman numeral equivalent

    >>> convert_to_roman_numeral(1)
    'I'
    >>> convert_to_roman_numeral(10000)
    'MMMMMMMMMM'
    >>> convert_to_roman_numeral(2134)
    'MMCXXXIV'
    """
    roman_symbols = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    roman_number = ""
    for (decimal, roman) in roman_symbols:
        (factor, number) = divmod(number, decimal)
        roman_number += roman * factor
    return roman_number


def colour_mixer():
    """Convert two primary colours into their relevant secondary colour.

    Computational thinking:
    Pattern Matching: since "yellow blue" and "blue yellow" both create green, I used an "or" statement in the if
        statement to combine these scenarios.
    Abstraction: instead of using an if/or statement, I could have split the input into a list, and then checked if each
        element of the list was in {"blue", "yellow", "red"} for example, which would have made the function more
        generalized because then only the values inside the curly brackets would need to be changed to check against
        other things.
    Automating with Algorithms: used the .lower() function to clean user input.

    :precondition: user input must be in the correct format (2 different primary colours), or if user input is not in
        the correct format, user input must be either repeated primary colours or some combination of secondary and
        primary colours to receive a helpful error message.
    :postcondition: correctly converts mixed primary colours to their corresponding secondary colour, or correctly
    provides the user with a helpful error message.
    """
    colour_input = input("enter two different primary colours separated by a space: (ex. yellow blue)").lower()
    if colour_input == "yellow blue" or colour_input == "blue yellow":
        print("green")
    elif colour_input == "blue red" or colour_input == "red blue":
        print("purple")
    elif colour_input == "yellow red" or colour_input == "red yellow":
        print("orange")
    elif colour_input == "yellow yellow" or colour_input == "blue blue"\
            or colour_input == "red red":
        print("sorry, both primary colours must be different from each other.")
    elif "green" in colour_input or "purple" in colour_input or "orange" in colour_input:
        print("sorry, both colours must be primary.")


def time_calculator(seconds):
    """Convert time in seconds into time in days, hours, minutes, and seconds.

    Computational thinking:
    Decomposition: used floor division to convert seconds into other units of time with the help of an
        intermediary value for seconds which used the modulus of the previous calculation.
    Abstraction: This function is similar to the convert_to_roman_numeral function and could be improved by
    Automating with Algorithms: I used an f string to simplify printing the converted time in the proper format

    :param seconds: positive integer to be converted
    :precondition: seconds must be a positive integer
    :postcondition: correctly calculates the time in days, hours, minutes, and seconds

    >>> time_calculator(0)
    0 0 0 0
    >>> time_calculator(3600)
    0 1 0 0
    >>> time_calculator(123456789)
    1428 21 33 9
    """
    days = seconds // 86400
    remaining_seconds = seconds % 86400

    hours = remaining_seconds // 3600
    remaining_seconds %= 3600

    minutes = remaining_seconds // 60
    remaining_seconds %= 60

    converted_time = f"{days} {hours} {minutes} {remaining_seconds}"
    print(converted_time)


def compound_interest(principal, interest_rate, compound_frequency, years_compounded):
    """Calculate compound interest.

    Computational thinking:
    Decomposition: Arithmetic operations were used to calculate the compound interest.
    Abstraction: By changing the parameters, function can be used to calculate compound interest for any initial value,
        interest rate, compound frequency, and years compounded.

    :param principal: a positive float
    :param interest_rate: a positive float
    :param compound_frequency: a positive integer
    :param years_compounded: a positive integer
    :precondition: principal and interest_rate must be positive floats, and compound_frequency and years_compounded
        must be positive integers
    :postcondition: calculates the correct compound interest as a float
    :return: correctly calculated compound interest as a float

    >>> compound_interest(1000.00, 0.1, 1, 2)
    1210.0000000000002
    >>> compound_interest(0, 0.1, 1, 2)
    0.0
    >>> compound_interest(1.00, 0, 1, 2)
    1.0
    """
    amount = principal * (1 + interest_rate / compound_frequency) ** (compound_frequency * years_compounded)
    return amount


def rock_paper_scissors():
    """Play a game of rock paper scissors vs the computer.

    Computational thinking:
    Decomposition: To simplify the number of conditional statements, I checked user input by seeing if it was in a list
        of permissible words.
    Pattern Matching: I Combined all victory scenarios into a single if statement using "and and "or" statements, and
        repeated this for all draw and loss scenarios.
    Abstraction: By changing what is asked of the user and the logic inside the nested for loop, this function can be
        used to perform various different tasks/games based on user input.
    Automating with Algorithms: The .lower and .strip functions were used to clean user input and make the program more
        user-friendly.

    :precondition: user input must be one of rock, paper, or scissors in order to play. Otherwise user input must be
        some other string in order to receive a helpful error message
    :postcondition: user has successfully played vs. the computer and knows whether they won, tied, or lost.  If the
        user typed an incorrect input, then they received a helpful error message
    """
    user_choice = input("enter one of rock, paper, or scissors").lower().strip()
    if user_choice in {"rock", "paper", "scissors"}:
        npc_choice = random.randint(0, 2)

        if npc_choice == 0:
            print("computer chose rock!")
        elif npc_choice == 1:
            print("computer chose paper!")
        elif npc_choice == 2:
            print("computer chose scissors!")

        if ((npc_choice == 0 and user_choice == "paper") or (npc_choice == 1 and user_choice == "scissors")
                or (npc_choice == 2 and user_choice == "rock")):
            print("you won!")
        elif ((npc_choice == 0 and user_choice == "rock") or (npc_choice == 1 and user_choice == "paper")
                or (npc_choice == 2 and user_choice == "scissors")):
            print("it's a draw!")
        else:
            print("you lost!")

    else:
        print("sorry, you must type either rock, paper, or scissors to play.")


def number_generator():
    """Generate a lotto ticket of six random integers between 1 and 49, sorted into a list of ascending numbers.

    Computational thinking:
    Abstraction: By changing the range and the sample size to be pulled out, this function can pull any size of sample
        out of any range, so long as the sample is smaller than the range.
    Automating with Algorithms: the .sort function automatically sorts the sample into the correct order.

    :postcondition: correctly generated and sorted list of six random integers between 1 and 49
    :return: sorted list of random integers between 1 and 49
    """

    lotto = random.sample(range(1, 49+1), 6)
    lotto.sort()
    return lotto


def number_translator_helper(i, raw_number_list):
    """Convert letters in a phone number to their corresponding number.

    Helper function to number_translator.

    :param i: integer index of raw_number_list
    :param raw_number_list: list of numbers, letters, and dashes
    :precondition: list of numbers, letters, and dashes to be translated
    :postcondition: correctly translated list of numbers and dashes
    """
    if raw_number_list[i] in {"A", "B", "C"}:
        raw_number_list[i] = "2"
    elif raw_number_list[i] in {"D", "E", "F"}:
        raw_number_list[i] = "3"
    elif raw_number_list[i] in {"G", "H", "I"}:
        raw_number_list[i] = "4"
    elif raw_number_list[i] in {"J", "K", "L"}:
        raw_number_list[i] = "5"
    elif raw_number_list[i] in {"M", "N", "O"}:
        raw_number_list[i] = "6"
    elif raw_number_list[i] in {"P", "Q", "R", "S"}:
        raw_number_list[i] = "7"
    elif raw_number_list[i] in {"T", "U", "V"}:
        raw_number_list[i] = "8"
    elif raw_number_list[i] in {"W", "X", "Y", "Z"}:
        raw_number_list[i] = "9"
    else:
        raw_number_list[i] = raw_number_list[i]


def number_translator():
    """Convert a user-inputted string of letters, numbers, and dashes into its equivalent string of numbers and dashes.

    Computational thinking:
    Decomposition: For this function I decomposed it by adding a helper function to do the letter-to-number
        conversion. I also split the input string into a list in order to assess each character individually.
    Pattern Matching: Since multiple letters all correspond to the same number (ex. ABC translate to 2), I was able to
        combine them in the if statements.
    Abstraction: This function can be used to convert any
    Automating with Algorithms: the .upper function automatically changes the letters in the user's input to
        uppercase in order to simplify what is needed to be checked. The .join function returns the list back into a
        string so that the translated number can be printed for the user.

    :precondition: user must enter a string of numbers and letters in the proper format
    :postcondition: calculates the correct phone number from the input phone number
    :return: correctly converted phone number as a string of numbers separated by dashes
    """
    raw_number = str.upper(input("enter a 10-character telephone number of letters and numbers "
                                 "in the format \"XXX-XXX-XXXX\":"))
    raw_number_list = list(raw_number)

    for i in range(len(raw_number_list)):
        number_translator_helper(i, raw_number_list)

    translated_number = ""
    translated_number = translated_number.join(raw_number_list)
    return translated_number


def main():
    """
    Test the functions in this module.
    """
    doctest.testmod()
    # convert_to_roman_numeral(2134)
    # colour_mixer()
    # time_calculator(12312)
    # compound_interest(1000.00, 0.10, 2, 10)
    # rock_paper_scissors()
    # number_generator()
    # number_translator()


if __name__ == "__main__":
    main()
