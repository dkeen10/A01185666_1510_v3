import time


def timer(func):
    """Print the runtime of the decorated function"""
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        file_name = "results.txt"
        with open(file_name, "a") as file_object:
            file_object.write(f"For {args[0]}, {func.__name__} took {run_time} seconds\n")
        return run_time
    return wrapper_timer


@timer
def factorial_iterative(num):
    """Find the factorial of a specified number.

    :param num: a positive, non-zero integer
    :postcondition:
    :return:
    """
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial


@timer
def factorial_recursive(num):
    factorial_recursive_helper(num)


def factorial_recursive_helper(num):
    if num == 1:
        return num
    else:
        return num * factorial_recursive_helper(num - 1)


def compare_time(iterative_total_time, recursive_total_time):
    file_name = "results.txt"
    with open(file_name, "a") as file_object:
        file_object.write(f"""factorial_iterative took {iterative_total_time} seconds in total.
factorial_recursive took {recursive_total_time} seconds in total.\n""")
        if iterative_total_time < recursive_total_time:
            file_object.write(f"Faster method was factorial_iterative")
        else:
            file_object.write(f"faster method was factorial_recursive")


def main():
    iterative_total_time = 0
    recursive_total_time = 0

    for num in range(1, 101):
        iterative_total_time += factorial_iterative(num)
        recursive_total_time += factorial_recursive(num)

    compare_time(iterative_total_time, recursive_total_time)


if __name__ == "__main__":
    main()
