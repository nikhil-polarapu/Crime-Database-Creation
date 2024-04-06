import src.assignment2_helper as assignment2
import pytest

# Testcase to check if correct values are extracted
def test_extractincidents():
    url = "https://www.normanok.gov/sites/default/files/documents/2024-02/2024-02-01_daily_incident_summary.pdf"
    data = [assignment2.fetchincidents(url)]
    result = assignment2.extractincidents(data)
    val = [5, 0, '0:14', '2024-00007318', '1152 W LINDSEY ST', 1, 'SW', 'Traffic Stop', False]
    assert val == result[0]