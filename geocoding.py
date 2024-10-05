import googlemaps
import array as arr
import os
from dotenv import find_dotenv, load_dotenv


def get_coordinates(address):

    # Load environment variables from .env file
    load_dotenv(find_dotenv())

    # Retrieve Google API KEY from env file
    api_key = os.getenv('GOOGLE_KEY')

    # Create a client object and pass API Key to it
    gmaps = googlemaps.Client(key = api_key)

    # Call geocode API, retrieve JSON response from address input
    geocode_json = gmaps.geocode(address)

    # Extract latitude and longitude from JSON result
    lat_lon_json = geocode_json[0]['geometry']['location']
    lat_lon_array = [lat_lon_json.get("lat"), lat_lon_json.get("lng")]

    # Return lat and lon
    return lat_lon_array