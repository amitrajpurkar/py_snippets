import requests # pip install requests
import json
from pprint import pprint

# https://home.openweathermap.org/api_keys
# api key: 04afad80f7b95195a3a9e49fa1659949  // for amit r.
# https://openweathermap.org/current
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
# http://api.openweathermap.org/geo/1.0/zip?zip={zip code},{country code}&appid={API key}
# https://www.iso.org/obp/ui/#search
# $HOMEBREW_PREFIX/opt/python@3.13/libexec/bin

BASE_URL = "https://api.openweathermap.org/"
API_KEY = "&appid=04afad80f7b95195a3a9e49fa1659949" 


def get_city_coords(zip):
    params = "geo/1.0/zip?zip={zip},US"
    url = BASE_URL + params + API_KEY
    response = requests.get(url)
    if response.status_code != 200:
        print("Error:", response.status_code)
        pprint(response.text)
        return

    data = json.loads(response.text)
    json_string = json.dumps(data, indent=2, sort_keys=True)
    pprint(json_string)
    return data

def get_weather_by_coords(zip):
    coords = get_city_coords(zip)
    lat = coords[0]["lat"]
    lon = coords[0]["lon"]

    params = "data/2.5/weather?lat={lat}&lon={lon}"
    url = BASE_URL + params + API_KEY
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def ask_zip_show_weather():
    zip = input("Enter zip code: ")
    data = get_weather_by_coords(zip)
    pprint(data)


ask_zip_show_weather()