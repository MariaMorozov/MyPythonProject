import requests
from geopy.geocoders import Nominatim


def geo(city):
    my_geolocator = Nominatim(user_agent="myGeocoder", timeout=500)
    # New York  Modiin Jerusalem Moscow
    location = my_geolocator.geocode(city)
    city_location = [location.latitude, location.longitude]
    return city_location


def send(key, host, city):
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

    querystring = {"lon": geo(city)[1], "lat": geo(city)[0]}

    headers = {
        'x-rapidapi-key': key,
        'x-rapidapi-host': host
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response = response.json()

    response = response['data'][0]

    city_name = response['city_name']
    country_code = response['country_code']
    temp = response['temp']
    weather = response['weather']['description']

    print(f"In {city_name}({country_code}) now {temp} degrees Celsius, {weather}.")
    return response


