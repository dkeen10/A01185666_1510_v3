from collections import Counter
import string
import typing


def read_file(file_name: str) -> str:
    """Open the specified text file.

    :param file_name: a string
    :precondition: file_name must be a string included in the list of available text files
    :postcondition: the specified text file has successfully been opened
    :return: the specified text file as a string
    """
    with open(file_name) as file_object:
        content = file_object.read()
        return content


def count_words(file_name: str) -> typing.Counter[str]:
    """Count the number of times each word appears in the specified text file.
    
    :param file_name: a string
    :precondition: file_name must be a string included in the list of available text files
    :postcondition: successfully counts how many times each word is in the specified text file
    :return: a count of how many times each word is in the specified text file
    """
    current_file = read_file(file_name)
    words = current_file.lower().strip().split()
    word_list = str.maketrans('', '', string.punctuation)
    stripped_list = [word.translate(word_list) for word in words]
    word_count = Counter(stripped_list)
    return word_count


def top_ten_words(file_name: str):
    """Count the number of times each word appears in the specified text file.

    :param file_name: a string
    :precondition: file_name must be a string included in the list of available text files
    :postcondition: correctly displays the top 10 most common words in the specified text file
    """
    top_n_words = 10
    top_10_word_dic = count_words(file_name).most_common(top_n_words)
    for key, value in top_10_word_dic:
        print(f"{key}: {value}")


def main():
    files = ["little_women.txt", "moby_dick.txt", "alice.txt", "siddhartha.txt"]
    print("Here are the available files:")
    for file in files:
        print(file)
    file_name = "gutenberg/" + input("Which file would you like to open?")
    try:
        top_ten_words(file_name)
    except FileNotFoundError:
        print("File was not found")


if __name__ == "__main__":
    main()
