from email.policy import default
import requests
import json

APPID = "5f95ff4264651e11c264acd968607324"  # <-- Put your OpenWeatherMap appid here!
URL_BASE = "http://api.openweathermap.org/geo/1.0/"


def current_coords(q: str = "Chicago", appid: str = APPID) -> dict:
    """https://openweathermap.org/api"""
    params = {}
    params['lat'] = requests.get(URL_BASE + "direct?", params=locals()).json()[0]['lat']
    params['lon'] = requests.get(URL_BASE + "direct?", params=locals()).json()[0]['lon']
    return params

def current_weather(lat: float(41.8755616),lon: float(-87.6244212),appid: str = APPID) -> dict:
    return requests.get("https://api.openweathermap.org/data/2.5/weather?",params=locals()).json()['main']

def weather_forecast(q: str = "Kolkata, India", appid: str = APPID) -> dict:
    """https://openweathermap.org/forecast5"""
    return requests.get(URL_BASE + "direct?", params=locals()).json()


def weather_onecall(lat: float = 55.68, lon: float = 12.57, appid: str = APPID) -> dict:
    """https://openweathermap.org/api/one-call-api"""
    return requests.get(URL_BASE + "onecall", params=locals()).json()

if __name__ == "__main__":
    from pprint import pprint

    while True:
        location = input("Enter a location:").strip()
        if location:
            data = current_coords(location)
            weather = current_weather(data['lat'], data['lon'])
            print(f"Temperature now is {weather['temp']-273.15}, feels like {weather['feels_like']-273.15}.\nMinimum temp is: {weather['temp_min']-273.15}, max is: {weather['temp_max']-273.15}")
        else:
            break