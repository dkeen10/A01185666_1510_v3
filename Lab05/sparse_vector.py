import doctest


def sparse_add(vector_one: dict, vector_two: dict) -> dict:
    """Add two specified sparse vectors.

    :param vector_one: a sparse vector in dictionary form with keys that are integers
    :param vector_two: a sparse vector in dictionary form with keys that are integers
    :precondition: vector_one and vector_two must be two well-formed sparse vectors
    :postcondition: calculates the correct sum of the two specified sparse vectors
    :return: the correct sum of the two specified sparse vectors
    >>> sparse_add({'length': 5, 2: 7.5, 4: -6}, {4: -5, 'length': 5, 0: 4.3})
    {'length': 5, 2: 7.5, 4: -11, 0: 4.3}
    >>> sparse_add({'length': 10, 9: -1}, {'length': 10, 9: 1})
    {'length': 10}
    >>> sparse_add({'length': 5}, {'length': 7}) is None
    True
    >>> sparse_add({'length': 0}, {'length': 0}) is None
    True
    >>> sparse_add({'length': 1}, {'length': 1})
    {'length': 1}
    """
    # to handle if vector_one does not have the same length as vector_two, or if both are zero length
    if vector_one['length'] != vector_two['length'] | (vector_one['length'] == 0 and vector_two['length'] == 0):
        return None

    # sparse addition logic:
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


def sparse_dot_product(vector_one: dict, vector_two: dict) -> int:
    """Calculate dot product of the two provided sparse vectors.

    :param vector_one: a sparse vector in dictionary form with keys that are integers
    :param vector_two: a sparse vector in dictionary form with keys that are integers
    :precondition: vector_one and vector_two must be two well-formed sparse vectors
    :postcondition: correctly calculates the dot product of the two specified sparse vectors as an int
    :return: the correctly calculated dot product of the two specified sparse vectors as an int or float
    >>> sparse_dot_product({'length': 5, 2: 7, 4: -6}, {4: -5, 'length': 5, 0: 4})
    30
    >>> sparse_dot_product({'length':0}, {'length':0}) is None
    True
    >>> sparse_dot_product({'length':5}, {'length':7}) is None
    True
    >>> sparse_dot_product({0: 2, 4: -1, 2: 1, 'length':5}, {1: 3, 'length':5, 3: 5})
    0
    >>> sparse_dot_product({'length':1}, {'length':1})
    0
    """
    # to handle if vector_one does not have the same length as vector_two, or if both are zero length
    if vector_one['length'] != vector_two['length'] | (vector_one['length'] == 0 and vector_two['length'] == 0):
        return None

    # sparse dot product logic:
    else:
        dot_product = 0
        for key in vector_one.keys():
            if key in vector_two.keys():
                if key != 'length':
                    dot_product += vector_one[key] * vector_two[key]
        return dot_product


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
