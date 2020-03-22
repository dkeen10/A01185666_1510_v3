import io
from collections import Counter
import string
import re
from itertools import islice

# regex: (?<=(\s))the(?=[\s\W$])


# def open_file(file_name):
#     return open(file_name)


# def read_file(file_name):
#     with open(file_name, "r") as file_object:
#         content = file_object.read()
#         return content


def remove_punctuation(current_file):
    """

    """
    punctuation = r"!?\"'][(){}**&^%$#.,:;"
    for word in current_file:
        word.translate(str.maketrans('', '', string.punctuation))

        # re.sub(r'[^\w\s]', '', word)
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace(":", "")
        word = word.replace("\"", "")
        word = word.replace("!", "")
        word = word.replace("'", "")
        word = word.replace("(", "")
        word = word.replace(")", "")
    return current_file

# def count_words(file_name):
#     """
#
#     """
#     word_count = {}
#     for word in read_file(file_name).lower().split():
#         word = word.replace(".", "")
#         word = word.replace(",", "")
#         word = word.replace(":", "")
#         word = word.replace("\"", "")
#         word = word.replace("!", "")
#         word = word.replace("'", "")
#         word = word.replace("(", "")
#         word = word.replace(")", "")
#         # word_count[word] = word_count.get(word, 0) + 1
#         if word not in word_count:
#             word_count[word] = 1
#         else:
#             word_count[word] += 1
#         return word_count


def read_file(file_name):
    with open(file_name) as file_object:
        content = file_object.read()
        return content


def count_words(file_name):
    # word_count = count_words(file_name)
    # n_print = 10
    # print("\nOK. The {} most common words are as follows\n".format(n_print))
    # word_counter = collections.Counter(word_count)
    # for word, count in word_counter.most_common(n_print):
    #     print(word, ": ", count)
    current_file = read_file(file_name)
    # remove_punctuation(current_file)
    words = current_file.lower().strip().split()
    word_list = str.maketrans('', '', string.punctuation)
    stripped_list = [word.translate(word_list) for word in words]
    word_count = Counter(stripped_list)
    return word_count


def top_ten_words(file_name):
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
    print(file_name)
    try:
        top_ten_words(file_name)
    except:
        raise TypeError


if __name__ == "__main__":
    main()
