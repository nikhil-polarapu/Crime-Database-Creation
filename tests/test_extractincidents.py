import src.assignment2_helper as assignment2
import pytest

# Testcase to check if correct values are extracted
def test_extractincidents():
    url = "https://www.normanok.gov/sites/default/files/documents/2024-02/2024-02-01_daily_incident_summary.pdf"
    data = [assignment2.fetchincidents(url)]
    result = assignment2.extractincidents(data)
    val = [5, 0, '0:10', '2024-00002259', '3300 HEALTHPLEX PKWY', 1, 'NW', 'Transfer/Interfacility', True]
    assert val == result[0]