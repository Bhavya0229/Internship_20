"""
Develop a Currency Converter which Converts an unit USD to INR

You need to fetch the current conversion prices from the JSON response
using REST API call.
"""

url = "http://data.fixer.io/api/latest?access_key=db94a57bc1b8d86510323a4c84adbe87&cbase=USD&symbols=INR"

import requests

response = requests.get(url)
jsondata = response.json()
print(jsondata['rates'])
