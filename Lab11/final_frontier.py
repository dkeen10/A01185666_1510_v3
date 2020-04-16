import requests
import json
import time


def get_mars_weather(url: str) -> (object, list):
    """Get the weather on mars from Nasa's InSight API.

    :param url: a string
    :precondition: url must be a well-formed url string linking to nasa's InSight API
    :postcondition: succesfully returns the correct temperature on mars on each sol in sol_keys
    :return: the correct temperature on mars on each sol in sol_keys
    """
    response = requests.get(url)
    response.raise_for_status()
    mars_weather = json.loads(response.text)
    sol_keys = mars_weather["sol_keys"]
    return mars_weather, sol_keys


def print_mars_temp(mars_weather: dict, sol_keys: list):
    """Print the temperature of mars on all available Sols.

    :param mars_weather: the temperature in celsius of each sol day
    :param sol_keys: a list of the sol days found in the InSight API
    :precondition: mars_weather and sol_keys have been successfully requested from InSight API
    :postcondition: the correct mars temperature on each sol in sol days have been printed
    """
    degree_sign = u"\N{DEGREE SIGN}"
    for i in range(0, len(sol_keys)):
        sol_weather = mars_weather[sol_keys[i]]["AT"]["av"]
        print(f"On sol {sol_keys[i]}, the temperature on mars was {sol_weather}{degree_sign}C ")
        print_every_five_min()


def print_every_five_min():
    """Set a timeout of five minutes.

    :precondition: the temperature of mars on a given sol has successfully been printed and is awaiting a timeout
    :postcondition: the print_mars_temp function has been timed out for five minutes
    """
    timeout = 300
    time.sleep(timeout)


def main():
    api_key = "H1OGNaGOn3Ode5NZYpRGNrgNCXeWyFFnYT207WaX"
    url = f"https://api.nasa.gov/insight_weather/?api_key={api_key}&feedtype=json&ver=1.0"
    mars_weather, sol_keys = get_mars_weather(url)
    print_mars_temp(mars_weather, sol_keys)


if __name__ == "__main__":
    main()
