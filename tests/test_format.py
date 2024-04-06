import src.assignment2_helper as assignment2
import src.format_data as formatData
import pandas as pd
import pytest

# Testcase to check if correct day is extracted
def test_check_day():
    day = formatData.dayOfWeek('04/06/2024')
    assert day == 7

# Testcase to check if correct hour is extracted
def test_check_hour():
    hour = formatData.hourOfDay('11:58')
    assert hour == 11

# Testcase to check if correct hour is extracted
def test_check_change_format():
    date = formatData.changeDateFormat('04/06/2024')
    assert date == '2024-04-06'

# Testcase to check if ranking is done correctly
def test_check_ranking():
    df = pd.DataFrame({
            'location': ['A', 'B', 'C', 'A', 'B', 'C', 'D']
    })
    result = formatData.rankData(df, 'location', 'location_rank')
    expected = pd.DataFrame({
            'location': ['A', 'B', 'C', 'A', 'B', 'C', 'D'],
            'location_rank': [1, 1, 1, 1, 1, 1, 4]
    })
    pd.testing.assert_frame_equal(result, expected)
