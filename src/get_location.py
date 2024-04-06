from geopy.geocoders import Nominatim
import re
import math

def get_location(address):
    # Initialize Nominatim geocoder
    geolocator = Nominatim(user_agent="Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17")
    address = address + " NORMAN, OK"
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
    ref_latitude = 35.220833
    ref_longitude = -97.443611
    d_lon = longitude - ref_longitude
    d_lat = latitude - ref_latitude
    
    # Convert latitude and longitude differences to radians
    d_lon_rad = math.radians(d_lon)
    d_lat_rad = math.radians(d_lat)
    
    # Calculate the angle relative to North
    angle = math.atan2(d_lon_rad, d_lat_rad)
    
    # Convert angle to degrees
    angle_deg = math.degrees(angle)
    
    # Adjust angle to be in the range [0, 360)
    if angle_deg < 0:
        angle_deg += 360
    
    # Define directions and their respective angles
    directions = {
        'N': (0, 22.5),
        'NE': (22.5, 67.5),
        'E': (67.5, 112.5),
        'SE': (112.5, 157.5),
        'S': (157.5, 202.5),
        'SW': (202.5, 247.5),
        'W': (247.5, 292.5),
        'NW': (292.5, 337.5),
        'N': (337.5, 360)
    }
    
    # Determine the direction based on the angle
    for direction, (lower, upper) in directions.items():
        if lower <= angle_deg < upper:
            return direction
    
    # If angle doesn't fall into any defined direction, return None
    return None

def is_location_format(location):
    pattern = r'^-?\d+\.\d+;-?\d+\.\d+$'
    return re.match(pattern, location) is not None

