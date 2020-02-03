"""
Functions to recreate and solve the Dutch National Flag Problem.
Duncan Keen
A01185666
"""


def dijkstra(dutch):
    """sort an unorganized list of elements red, white, and blue into a sorted list and then manipulate the list to be
     in the order: all the reds, then all the whites, then all the blues.

    :param dutch: unsorted list of strings red, white, and/or blue.
    :precondition: parameter must be a list of strings of only red, white, and/or blue.
    :postcondition: correctly organized list of strings in the the proper order of colours.

    >>> test_list = ["red"]
    >>> dijkstra(test_list)
    >>> print(test_list)
    ['red']
    >>> test_list = ["white", "white", "white", "white"]
    >>> dijkstra(test_list)
    >>> print(test_list)
    ['white', 'white', 'white', 'white']
    >>> test_list=["white", "red", "white", "blue", "white", "red", "white"]
    >>> dijkstra(test_list)
    >>> print(test_list)
    ['red', 'red', 'white', 'white', 'white', 'white', 'blue']
    >>> test_list=["blue", "white"]
    >>> dijkstra(test_list)
    >>> print(test_list)
    ['white', 'blue']
    >>> test_list=["blue"]
    >>> dijkstra(test_list)
    >>> print(test_list)
    ['blue']
    """
    dutch.sort()
    for i in range(0, len(dutch)+1, 1):
        if dutch[0] == "blue":
            dutch.remove("blue")
            dutch.append("blue")


def main():
    """
    test this module.
    """
    import doctest
    doctest.testmod()

    dutch = ["blue", "red", "blue", "white"]
    dijkstra(dutch)
    print(dutch)


if __name__ == "__main__":
    main()
