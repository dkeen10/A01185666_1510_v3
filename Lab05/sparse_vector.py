import doctest
from typing import Union


def sparse_add(vector_one: dict, vector_two: dict) -> Union[dict, None]:
    """Add two sparse vectors.

    :param vector_one: a sparse vector in dictionary form
    :param vector_two: a sparse vector in dictionary form
    :precondition: vector_one and vector two must be two well-formed sparse vectors in dictionary form
    :postcondition: calculates the correct sum of the two specified sparse vectors
    :return: the correct sum of the two specified sparse vectors
    >>> sparse_add({'length': 5, 2: 7.5, 4: -6}, {4: -5, 'length': 5, 0: 4.3})
    {'length': 5, 2: 7.5, 4: -11, 0: 4.3}
    >>> sparse_add({'length': 10, 7:-1}, {'length': 10, 7: 1})
    {'length': 10}
    >>> sparse_add({'length':5}, {'length':7})

    """
    if vector_one['length'] != vector_two['length']:
        return None

    else:
        combined_vector = {}
        for key, value in vector_one.items():
            combined_vector[key] = value
        for key, value in vector_two.items():
            if key in combined_vector and key != 'length':
                combined_vector[key] += vector_two[key]
                if combined_vector[key] == 0:
                    del combined_vector[key]
            else:
                combined_vector[key] = value
    return combined_vector


def sparse_dot_product(vector_one: dict, vector_two: dict) -> Union[int, float, None]:
    """Calculate dot product of the two provided sparse vectors.

    :param vector_one: a sparse vector in dictionary form
    :param vector_two: a sparse vector in dictionary form
    :precondition: vector_one and vector two must be two well-formed sparse vectors in dictionary form
    :postcondition: correctly calculates the dot product of the two specified sparse vectors
    :return: the correctly calculated dot product of the two specified sparse vectors
    >>> sparse_dot_product({'length': 5, 2: 7.5, 4: -6}, {4: -5, 'length': 5, 0: 4.3})
    30
    >>> sparse_dot_product({'length':0}, {'length':0})
    0
    >>> sparse_dot_product({'length':5}, {'length':7})

    >>> sparse_dot_product({4: -1, 2: 1.5, 'length':5}, {2: 3, 'length':5, 1: 5})
    4.5
    """
    if vector_one['length'] != vector_two['length']:
        return None

    else:
        dot_product = 0
        for key in vector_one.keys():
            if key in vector_two.keys():
                if key != 'length':
                    dot_product += vector_one[key] * vector_two[key]
        return dot_product


def main():
    doctest.testmod()
    sparse_add({'length': 5, 2: 7.5, 4: -6}, {4: -5, 'length': 5, 0: 4.3})
    sparse_dot_product({'length': 5, 2: 7.5, 4: -6}, {4: -5, 'length': 5, 0: 4.3})


if __name__ == "__main__":
    main()
