import requests
import json

def solar_estimation():

    lat_long = json.dumps({
        "latitude": 28.603330,
        "longitude": -81.239190
    })

    response = requests.get(https://solar.googleapis.com/v1/dataLayers:get?)