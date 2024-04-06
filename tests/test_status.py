import src.assignment2_helper as assignment2
import pytest

# Testcase to check if correct dataframe is created
def test_status():
    db = assignment2.createdb()
    incidents = [[5, 0, '0:10', '2024-00002259', '3300 HEALTHPLEX PKWY', 1, 'NW', 'Transfer/Interfacility', True]]
    assignment2.populatedb(incidents)
    result = assignment2.status()
    result = result.to_dict(orient='records')
    assert result[0] == {'Day of the Week': 5, 'Time of Day': 0, 'Weather': 1, 'Location Rank': 1, 'Side of Town': 'NW', 'Incident Rank': 1, 'Nature': 'Transfer/Interfacility', 'EMSSTAT': 1}
