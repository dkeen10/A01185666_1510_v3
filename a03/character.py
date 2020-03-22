import random
import doctest


def generate_vowel() -> str:
    """Generate a random vowel.

    :return: a string of one vowel letter

    """
    vowel_string = 'aeiouy'
    return ''.join(random.sample(vowel_string, 1))


def generate_consonants() -> str:
    """Generate a random consonant.

    :return: a string of one consonant letter

    """
    consonant_string = 'bcdfghjklmnpqrstvwxzy'
    return ''.join(random.sample(consonant_string, 1))


def generate_syllable() -> str:
    """Generate a random syllable.

    :return: A string of a syllable containing one consonant and one vowel.

    """
    return generate_consonants() + generate_vowel()


def generate_name(syllables: int) -> str:
    """Create a random name of given syllable number length.

    :param syllables: Positive integer that represents the number of syllables
    :precondition: Given number of syllables must be a positive integer
    :postcondition: random capitalized name of syllable number length
    :return: A random capitalized name in a string of give number of syllables

    """
    name = ''
    for i in range(0, syllables):
        name = name + generate_syllable()
    return name.capitalize()


def create_character(syllables: int) -> dict:
    """Create a character.

    :param syllables: A positive integer for the number of syllables in the name
    :precondition: Must give positive integer for number of syllables in name
    :postcondition: returns a character with a name with given number of syllables
    :return: A dictionary of a character

    """
    return {'Name': generate_name(syllables), 'HP': 10, 'Location': [2, 2]}


def print_character(character: dict):
    """Print stylized text showing the user their created character.

    :param character: a fully formed character in dictionary form
    :precondition: character must be a fully formed character in dictionary form
    :postcondition: a correctly printed and stylized version of the specified character

    Computational Thinking:
    Algorithms: I used the .keys method to print the character information in a more user friendly way.

    >>> print_character({'Name': 'ba', 'HP': 10, 'Location': [2, 2]})
    <=+=+=+=+=+=+=+=+=>
    Name ba
    HP 10
    Location [2, 2]
    <=+=+=+=+=+=+=+=+=>
    """
    print("<=+=+=+=+=+=+=+=+=>")
    for key in character.keys():
        print(key, character[key])
    print("<=+=+=+=+=+=+=+=+=>")


if __name__ == "__main__":
    doctest.testmod()
