import requests
import json
import os
from dotenv import load_dotenv
import pprint


def solar_api_request(lat_long):
    load_dotenv()

    APIKEY = os.getenv("GOOGLE_KEY")

    global response

    response = requests.get("https://solar.googleapis.com/v1/buildingInsights:findClosest?"+
                            "location.latitude=" + str(lat_long[0]) +
                            "&location.longitude="+ str(lat_long[1])+
                            "&requiredQuality=HIGH"
                            "&key=" + APIKEY)
    
    return


def solar_estimation(lat_long, num_panels):
    ''' Estimates the amount of energy is generated by a home's solar panels yearly
        with the specified latitudinal and longitudinal location and number of solar panels.
    '''

    # panel count

    solar_potential = response.json()['solarPotential']['solarPanelConfigs']

    for panel_config in solar_potential:
        if panel_config.get('panelsCount') == num_panels:
            return panel_config.get('yearlyEnergyDcKwh')

    pprint.pprint(solar_potential)
    # for panel_count in response.json().get("solarPotential"):

    
    # monthly to yearly

    # DC to AC electricity conversion




    # return solar_potential



def solar_max_panels():
    return response.json()['solarPotential'].get('maxArrayPanelsCount')


# def solar_finances():