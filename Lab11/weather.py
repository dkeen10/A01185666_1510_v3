"""
coords:  [49.2497, -123.1193]
api key: e36aed7c864d0f7a354272865d511189
Nasa API:gdYrt7eHWAQM9itM3O0IQCtDq71pF03AlkebavWF
ex. https://api.nasa.gov/planetary/apod?api_key=gdYrt7eHWAQM9itM3O0IQCtDq71pF03AlkebavWF
"""
import requests
import json


def get_input() -> int:
    try:
        user_input = int(input("How many days to forecast?"))
        if not 1 <= user_input <= 7:
            raise ValueError("days to forecast must be within 1-7")
    except ValueError:
        print("please enter a choice between 1-7")
        return 0
    return user_input


def get_weather(url: str) -> None:
    response =requests.get(url)
    response.raise_for_status()
    vancouver_weather = json.loads(response.txt)
    print(vancouver_weather)


def main():
    vancouver = 6173331
    api_key = "e36aed7c864d0f7a354272865d511189"
    url = f"http://api.openweathermap.org/data/2.5/forecast?id={vancouver}&APPID={api_key}"
    user_input = None
    while 7 <= user_input <= 1:
        user_input = get_input()
    get_weather(url)


if __name__ == "__main__":
    main()