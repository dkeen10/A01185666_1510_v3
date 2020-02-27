import doctest


def sparse_add(vector_one: dict, vector_two: dict):
    """Add two sparse vectors.

    :precon: well-formed dictionary

    >>> sparse_add({'length': 5, 2: 7.5, 4: -6}, {4: -5, 'length': 5, 0: 4.3})
    {'length': 5, 2: 7.5, 4: -11, 0: 4.3}
    >>> sparse_add({'length': 10, 7:-1}, {'length': 10, 7: 1})
    {'length': 10}
    """
    if vector_one['length'] != vector_two['length']:    # first line of code should check that parameter are the same length.
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


def sparse_dot_product(vector_one, vector_two):
    """Calculate dot product of the two provided sparse vectors.

    :precondition: vector_one and vector two must be two well-formed sparse vectors in dictionary form.
    :postcondition:
    :return: the correctly calculated dot product
    >>> sparse_dot_product({'length': 5, 2: 7.5, 4: -6}, {4: -5, 'length': 5, 0: 4.3})
    30
    >>> sparse_dot_product({'length':0}, {'length':0})
    0
    >>> sparse_dot_product({'length':5}, {'length':7})

    """
    if vector_one['length'] != vector_two['length']:    # first line of code should check that parameter are the same length.
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
