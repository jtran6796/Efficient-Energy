import requests
import json
import os
from dotenv import load_dotenv

def solar_estimation(lat_long):

    load_dotenv()

    APIKEY = os.getenv("GOOGLEKEY")

    response = requests.get("https://solar.googleapis.com/v1/buildingInsights:findClosest?"+
                            "location.latitude=" + str(lat_long[0]) +
                            "&location.longitude="+ str(lat_long[1])+
                            "&requiredQuality=HIGH"
                            "&key=" + APIKEY)
    

    print(response)

solar_estimation([37.4450, -122.1390])