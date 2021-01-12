import requests
from geopy.geocoders import Nominatim
import http.client
from logs import logger


def geo(city):
    my_geolocator = Nominatim(user_agent="myGeocoder", timeout=500)
    # New York  Modiin Jerusalem Moscow
    location = my_geolocator.geocode(city)
    city_location = [location.latitude, location.longitude]
    return city_location


def send(key, host, city):
    logger.info("Requested city for " + city)

    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

    querystring = {"lon": geo(city)[1], "lat": geo(city)[0]}

    headers = {
        'x-rapidapi-key': key,
        'x-rapidapi-host': host
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response = response.json()

    # response = response['data'][0]
    # print(response)
    # city_name = response['city_name']
    # country_code = response['country_code']
    # temp = response['temp']
    # weather = response['weather']['description']
    #
    # print(f"In {city_name}({country_code}) now {temp} degrees Celsius, {weather}.")
    return response


# send("9b8549f446mshf1f8fca475723dap1759b1jsn1f7a19aa0e50", "weatherbit-v1-mashape.p.rapidapi.com", 'Modiin')
