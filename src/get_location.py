from geopy.geocoders import Nominatim
import re

def get_location(address):
    # Initialize Nominatim geocoder
    geolocator = Nominatim(user_agent="Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17")

    # Try to geocode the address
    try:
        location = geolocator.geocode(address)
        if location:
            latitude = location.latitude
            longitude = location.longitude
            return latitude, longitude
        else:
            return None, None
    except Exception as e:
        return None, None

def get_direction(latitude, longitude):
    # Calculate the differences in latitude and longitude
    ref_latitude = 35.220833
    ref_longitude = -97.443611
    delta_lat = latitude - ref_latitude
    delta_lon = longitude - ref_longitude

    # Determine the direction
    if delta_lat > 0:
        if delta_lon > 0:
            return "NE"
        elif delta_lon < 0:
            return "NW"
        else:
            return "N"
    elif delta_lat < 0:
        if delta_lon > 0:
            return "SE"
        elif delta_lon < 0:
            return "SW"
        else:
            return "S"
    else:
        if delta_lon > 0:
            return "E"
        elif delta_lon < 0:
            return "W"
        else:
            return "Same location"

def is_location_format(location):
    pattern = r'^-?\d+\.\d+;-?\d+\.\d+$'
    return re.match(pattern, location) is not None

