"""
Demonstrate how to mock an object.
"""


def ask_for_value_and_convert_to_upper():
    return input("Enter your name please").strip().upper()
