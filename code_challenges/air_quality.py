"""
Take the name of the city from the user through cmd and show the 
    air quality parameteres using openmapweather api. 
    This API requires 
    lat long of place to get air quality.
    
    You need to search for an API to convert your city name 
    to Lat-Long.
"""
city_name = input("Enter city name: ")

import requests
geo_city = "http://api.openweathermap.org/geo/1.0/direct?q="+city_name+"&limit=1&appid=fe5bb972997e11a8696797c836ea19df"

response = requests.get(geo_city)
data = response.json()[0]

# getting latitude and longitude
lat_city = str(response.json()[0]['lat'])
lon_city = str(response.json()[0]['lon'])

# api for checking air pollution
url = "http://api.openweathermap.org/data/2.5/air_pollution?lat="+lat_city+"&lon="+lon_city+"&appid=fe5bb972997e11a8696797c836ea19df"

res = requests.get(url)
jsondata = res.json()