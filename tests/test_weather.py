import src.assignment2_helper as assignment2
import src.get_weather as getWeather
import pytest

# Testcase to check if correct weather code is returned
def test_weather_code():
    wmo = getWeather.get_weather_hour(35.2590797, -97.48936289809109, '2024-02-01', 0)
    assert wmo == 1
