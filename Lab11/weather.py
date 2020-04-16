import requests
import json


def get_input() -> int:
    """Get User Input.

    :postcondition: Correctly returns user_input if user has entered input between 1 and 7, else zero
    :raise ValueError: if userInput is less than 1 or greater than 7
    :return: user input if value is between 1 and 7, else zero
    """
    try:
        user_input = int(input("How many days to forecast?"))
        if 1 > user_input:
            raise ValueError("days to forecast must be a positive, non-zero integer")
        elif user_input > 7:
            raise ValueError("days to forecast must be 7 days or less")
    except ValueError:
        print("please enter a choice between 1-7")
        return 0
    return user_input


def get_weather(url: str) -> dict:
    """Get weather information from OpenWeatherMap API.

    :param url: a URL string containing the API key
    :precondition: url must be a string
    :postcondition: successfully returns the weather conditions for Vancouver as a list
    :return: a list of the weather conditions in Vancouver
    """
    response = requests.get(url)
    response.raise_for_status()
    vancouver_weather = json.loads(response.text)
    weather_list = vancouver_weather["list"]
    return weather_list


def print_weather(weather_list: dict, user_input: int):
    """Print the weather conditions in Vancouver over the course of the specified timeframe.

    :param weather_list: a dictionary
    :param user_input: an integer
    :precondition: weather_list must be a well-formed dictionary and user_input must be an integer between 1 and 7
    :postcondition: the weather conditions over the specified timeframe.
    """
    degree_sign = u"\N{DEGREE SIGN}"
    for i in range(0, user_input*8):
        print(f"the weather at {weather_list[i]['dt_txt']} is:")
        print(weather_list[i]['weather'][0]['main'], '-', weather_list[i]['weather'][0]['description'])
        print(f"{weather_list[i]['main']['temp']}{degree_sign}C, feels like {weather_list[i]['main']['feels_like']}{degree_sign}C")


def main():
    vancouver = 6173331
    api_key = "e36aed7c864d0f7a354272865d511189"
    url = f"http://api.openweathermap.org/data/2.5/forecast?id={vancouver}&APPID={api_key}&units=metric"
    user_input = 0
    while 7 <= user_input or user_input <= 1:
        user_input = get_input()
    print_weather(get_weather(url), user_input)


if __name__ == "__main__":
    main()
