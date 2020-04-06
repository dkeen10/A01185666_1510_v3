"""
coords:  [49.2497, -123.1193]
api key: e36aed7c864d0f7a354272865d511189
"""
import Requests


def get_input() -> int:
    try:
        user_input = int(input("How many days to forecast?"))
        if not 1 <= user_input <= 7:
            raise ValueError("days to forecast must be within 1-7")
    except ValueError:
        print("please enter a choice between 1-7")
        return 0
    return user_input


def get_weather():


def main():
    user_input = None
    while 7 <= user_input <= 1:
        user_input = get_input()


if __name__ == "__main__":
    main()