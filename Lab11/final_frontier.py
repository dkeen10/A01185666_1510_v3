import requests
import json
import datetime
import time

"""
H1OGNaGOn3Ode5NZYpRGNrgNCXeWyFFnYT207WaX
https://api.nasa.gov/planetary/apod?api_key=H1OGNaGOn3Ode5NZYpRGNrgNCXeWyFFnYT207WaX
"""


def get_mars_weather(url):
    response = requests.get(url)
    response.raise_for_status()
    mars_weather = json.loads(response.text)
    print(mars_weather)
    mars_temp = mars_weather[]
    print
    return mars_weather


def print_every_five_min():
    time.sleep(5)


def main():
    """

    """
    api_key = "H1OGNaGOn3Ode5NZYpRGNrgNCXeWyFFnYT207WaX"
    end_date = "2020-04-12"
    start_date = "2020-03-04"
    # url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    # url = f"https://api.nasa.gov/DONKI/FLR?startDate={start_date}&endDate={end_date}&api_key={api_key}"
    url = f"https://api.nasa.gov/insight_weather/?api_key={api_key}&feedtype=json&ver=1.0"
    get_mars_weather(url)


if __name__ == "__main__":
    main()
