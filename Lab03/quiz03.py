"""
Duncan Keen
Mike Sampson
Jasmanjeet Kaur Bath
"""


def average_top_three(first, second, third, fourth):
    """
    >>> average_top_three(10, 20, 25, 30)
    25.0
    >>> average_top_three(30, 30, 30, 30)
    30.0
    >>> average_top_three(30, 25, 20, 10)
    25.0
    """
    numbers = [first, second, third, fourth]
    numbers.sort(reverse=True)
    numbers.pop(3)
    return sum(numbers) / 3


def first_occurrence_index(sentence, substring):
    """
    >>> first_occurrence_index("hi", "bye")
    -1
    >>> first_occurrence_index("hello", "hello")
    0
    >>> first_occurrence_index("hello i am Duncan", "a")
    8
    """
    if substring not in sentence:
        return -1
    else:
        return sentence.index(substring)


def main():
    ids = [4353, 2314, 2956, 3382, 9362, 3900]
    print(ids)
    ids.remove(3382)
    print(ids)
    index = ids.index(9362)
    print(index)
    ids.insert(index+1, 4499)
    print(ids)
    ids.extend((5566, 1830))
    print(ids)
    ids.reverse()
    print(ids)
    ids.sort()
    print(ids)


if __name__ == "__main__":
    main()
