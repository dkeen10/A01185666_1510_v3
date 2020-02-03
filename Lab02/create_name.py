import random
import string

length = int(input("how long do you want the random name to be?"))
letters = string.ascii_lowercase


def create_name():
    """
    Asks user for length of name and returns a random name of that length
    :return: a random name of given length
    """
    random_name = "".join(random.choice(letters) for x in range(length))
    print(f"generated name is {random_name.title()}")


if __name__ == "__main__":
    create_name()

