def factorial_iterative(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    print(factorial)


def factorial_recursive(num):
    while i > 0:
        factorial_recursive(num)


def main():
    for num in range(1, 101):
        factorial_iterative(num)
        factorial_recursive(num)


if __name__ == "__main__":
    main()