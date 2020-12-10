import requests
from geopy.geocoders import Nominatim
import argparse

parser = argparse.ArgumentParser(description='Weather in your city')

geolocator = Nominatim(user_agent="ISRAEL")

my_input = "Modiin"
# my_input = input("Please enter your city: ")  # New York  Modiin Jerusalem Moscow
location = geolocator.geocode(my_input)

try:
    print(f"{my_input} latitude :{location.latitude}, longitude: {location.longitude}")

    parser.add_argument('-lat', '--latitude', action='store', dest='latitude', help='latitude',
                        default=location.latitude)
    parser.add_argument('-lon', '--longitude', action='store', dest='longitude', help='longitude',
                        default=location.longitude)

    results = parser.parse_args()

    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

    querystring = {"lang": "en", "lon": results.longitude,
                   "lat": results.latitude}  # "lon":"35.01051"  "lat":"31.89825"

    headers = {
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
        'x-rapidapi-key': "9b8549f446mshf1f8fca475723dap1759b1jsn1f7a19aa0e50"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #   print(type(response))
    #   print(response.text)
    #   ##################

    response = response.json()
    response = response['data'][0]

    city_name = response['city_name']
    country_code = response['country_code']
    temp = response['temp']
    weather = response['weather']['description']

    print(f"In {city_name}({country_code}) now {temp} degrees Celsius, {weather}.")


except Exception as ex:
    print("Wrong location!")
    print(ex)



