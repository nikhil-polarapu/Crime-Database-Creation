import src.assignment2_helper as assignment2
import src.get_location as getLocation
import pytest

# Testcase to check if correct coordinates are returned
def test_location():
    [lat, lon] = getLocation.get_location('3300 HEALTHPLEX PKWY')
    assert [lat, lon] == [35.2590797, -97.48936289809109]

# Testcase to check if correct direction is returned
def test_direction():
    direction = getLocation.get_direction(35.2590797, -97.48936289809109)
    assert direction == 'NW'


