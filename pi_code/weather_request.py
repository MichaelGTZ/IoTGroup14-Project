import time
import requests
from pprint import pprint

settings = {
    'api_key':'4d068421457c492abdb7df3bbfdf77e2',
    'zip_code':'10025',
    'country_code':'us',
    'temp_unit':'imperial'} #unit can be metric, imperial, or kelvin

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid={0}&zip={1},{2}&units={3}"

def get_weather():
    final_url = BASE_URL.format(settings["api_key"],settings["zip_code"],settings["country_code"],settings["temp_unit"])
    weather_data = requests.get(final_url).json()
    description = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp']
    return (description, str(temp))