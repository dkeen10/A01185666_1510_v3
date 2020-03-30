import time
import math


# def write_file():
#     "Read and write to text file"
#     file_name = "results.txt"
#     with open(file_name) as file_object:
#         file_object.write()


def timer(func):
    """Print the runtime of the decorated function"""
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        file_name = "results.txt"
        with open(file_name) as file_object:
            file_object.write(f"{func.__name__} took {run_time} seconds")
        # return run_time, func.__name__
    return wrapper_timer


@timer
def eratosthenes_duncan(upper_bound):
    non_prime_numbers = []
    prime_numbers = []

    for i in range(2, upper_bound+1):
        if i not in non_prime_numbers:
            prime_numbers.append(i)
            for j in range(i * i, upper_bound+1, i):
                non_prime_numbers.append(j)
    return prime_numbers


@timer
def eratosthenes_mike(upper_bound):
    numbers = list(range(2, upper_bound + 1))
    upper_bound_sqrt = math.ceil(math.sqrt(upper_bound))
    for number in range(2, upper_bound_sqrt):
        if number in numbers:
            for to_remove in range(number * 2, upper_bound + 1, number):
                if to_remove in numbers:
                    numbers.remove(to_remove)
    return numbers


@timer
def eratosthenes_luke(upper_bound):
    prime = [True] * (upper_bound + 1)
    number = 2
    while number * number <= upper_bound:
        if prime[number]:
            for not_prime_number in range(number * number, upper_bound + 1, number):
                prime[not_prime_number] = False
        number += 1
    prime = [prime_numbers for prime_numbers in range(2, upper_bound + 1)
             if prime[prime_numbers]]
    return prime


def main():
    upper_bound = 1000
    fastest_time = None
    fastest_eratosthenes = None

    for eratosthenes in {eratosthenes_mike, eratosthenes_luke, eratosthenes_duncan}:
        run_time, func_name = eratosthenes(upper_bound)
        if not fastest_time or run_time < fastest_time:
            fastest_time = run_time
            fastest_eratosthenes = func_name

    print(f"Fastest function was {fastest_eratosthenes}!")


if __name__ == "__main__":
    main()
