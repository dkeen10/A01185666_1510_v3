import time
import doctest


def timer(func):
    """Write the runtime of the decorated function to a text file."""
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        end_time = time.perf_counter()
        run_time = end_time - start_time
        file_name = "results.txt"
        with open(file_name, "a") as file_object:
            file_object.write(f"For {args[0]}, {func.__name__} took {run_time} seconds\n")
        return run_time
    return wrapper_timer


@timer
def factorial_iterative(num: int) -> int:
    """Find the factorial of a specified number using iterative methods.

    :param num: a positive, non-zero integer
    :precondition: num must be a positive, non-zero integer
    :postcondition: the factorial has been correctly calculated and the time taken has been successfully recorded
    :return: the factorial of the specified number, or with the wrapper in place, the time it takes

    >>> factorial_iterative(1)
    1
    >>> factorial_iterative(0)
    1
    >>> factorial_iterative(4)
    24
    """
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial


@timer
def factorial_recursive(num: int) -> int:
    """Calculate factorial of the specified number using recursive methods.

    :param num: a positive, non-zero integer
    :precondition: num must be a positive, non-zero integer
    :postcondition: the factorial has been correctly calculated and the time taken has been successfully recorded
    :return: the factorial of the specified number, or with the timer decorator in place, the time the function takes

    >>> factorial_recursive(0)
    1
    >>> factorial_recursive(1)
    1
    >>> factorial_recursive(4)
    24
    """
    return factorial_recursive_helper(num)


def factorial_recursive_helper(num: int) -> int:
    """Helper function to factorial_recursive.

    :param num: a positive, non-zero integer
    :precondition: num must be a positive, non-zero integer
    :postcondition: the factorial has been correctly calculated and the time taken has been successfully recorded
    :return: the factorial of the specified number, or with the timer decorator in place, the time the function takes

    >>> factorial_recursive_helper(0)
    1
    >>> factorial_recursive_helper(1)
    1
    >>> factorial_recursive_helper(4)
    24
    """
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial_recursive_helper(num - 1)


def compare_time(iterative_total_time: float, recursive_total_time: float):
    """Compare the time it took for the specified functions to complete.

    :param iterative_total_time: a positive, non-zero float
    :param recursive_total_time: a positive, non-zero float
    :precondition: iterative_total_time and recursive_total_time must be positive, non-zero floats
    :postcondition: the time it took for the specified functions to complete has been accurately calculated
    """
    file_name = "results.txt"
    with open(file_name, "a") as file_object:
        file_object.write(f"""factorial_iterative took {iterative_total_time} seconds in total.
factorial_recursive took {recursive_total_time} seconds in total.\n""")
        if iterative_total_time < recursive_total_time:
            file_object.write(f"Faster method was factorial_iterative")
        else:
            file_object.write(f"faster method was factorial_recursive")


def main():
    doctest.testmod()
    iterative_total_time = 0
    recursive_total_time = 0

    for num in range(1, 101):
        iterative_total_time += factorial_iterative(num)
        recursive_total_time += factorial_recursive(num)

    compare_time(iterative_total_time, recursive_total_time)


if __name__ == "__main__":
    main()
