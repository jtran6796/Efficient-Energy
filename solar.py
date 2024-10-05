import requests
import json
import os
from dotenv import load_dotenv

def solar_estimation(lat_long):

    load_dotenv()

    APIKEY = os.getenv("GOOGLE_KEY")

    response = requests.get("https://solar.googleapis.com/v1/buildingInsights:findClosest?"+
                            "location.latitude=" + str(lat_long[0]) +
                            "&location.longitude="+ str(lat_long[1])+
                            "&requiredQuality=HIGH"
                            "&key=" + APIKEY)
    
    
    # panel count
    print("test")
    
    for panel_count in response.json().get("solarPotential"):

        if panel_count == 13:
            print(panel_count['yearlyEnergyDcKwh'])

    # for panel_statistics in response.json():
    #     if panel_statistics['panelsCount']  == 13:
    #         print(panel_statistics['yearlyEnergyDcKwh'])

    # monthly to yearly

    # DC to AC electricity conversion
    return response.json()




solar_estimation([37.4450, -122.1390])