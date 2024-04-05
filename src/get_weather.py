import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import requests

def get_weather_code(latitude, longitude, date):
    
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": date,
        "end_date": date,
        "hourly": "weather_code",
        "timezone": "America/Chicago"
    }
    data = requests.get(url, params).json()
    return data

def get_weather_hour(latitude, longitude, date, hour):
    weather_data = get_weather_code(latitude, longitude, date)
    #print(weather_data['hourly']['weather_code'][hour])
    return weather_data['hourly']['weather_code'][hour]
