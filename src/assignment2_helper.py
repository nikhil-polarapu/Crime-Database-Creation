import urllib.request
import io
import re
from pypdf import PdfReader
import sqlite3
import os
import sys
import pandas as pd
import src.format_data as fd
import src.get_location as getLocation
import src.get_weather as getWeather

# Function to fetch data from URL
def fetchincidents(url):
    url = (url)
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    return io.BytesIO(data)                                                                         

# Function to extract tabular data from the result of fetchincidents
def extractincidents(data):
    np = 0
    row_list = []
    input_list = []
    for datum in data:
        reader = PdfReader(datum)

        for page_num in range(len(reader.pages)):
            page = reader._get_page(page_num)
            page_text = page.extract_text(extraction_mode='layout')
            lines = page_text.split("\n")

            for line in lines:

                line = line.strip()

                if("NORMAN POLICE DEPARTMENT" in line):
                    line = line.replace("NORMAN POLICE DEPARTMENT", '')
                if("Daily Incident Summary (Public)" in line):
                    line = line.replace("Daily Incident Summary (Public)", '')
                if("Date / Time Incident Number Location Nature Incident ORI" in line):
                    line = line.replace("Date / Time Incident Number Location Nature Incident ORI", '')
                
                input_list.append(line)
        
    for line in input_list:
            
        output = []
        
        # Extracting date
        datetime_pattern = r'\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{2}'
        datetime_match = re.search(datetime_pattern, line)

        datetime = []

        if(datetime_match):
            datetime_result = datetime_match.group()
            [date, time] = datetime_result.split()
            output.append(fd.dayOfWeek(date)) # Day of the Week 
            hour = fd.hourOfDay(time)
            output.append(hour) # Time of Day
            output.append(time) # Time with minutes
            date = fd.changeDateFormat(date)
            line = line.replace(datetime_result, '').strip()
            
        # Extracting incident number
        incident_number_pattern = r'\d{4}-\d+'
        incident_number_match = re.search(incident_number_pattern, line)

        if(incident_number_match):
            incident_number_result = incident_number_match.group()
            output.append(incident_number_result) # Incident Number
            line = line.replace(incident_number_result, '').strip()

        # Extracting location, nature and incident_ori
        if(line):
            remaining_line = re.split(r'\s{2,}', line.strip())
            if(len(remaining_line) == 3):
                location = remaining_line[0]
                output.append(location) # Location
                if(getLocation.is_location_format(location)):
                    [latitude, longitude] = location.split(';')
                    [latitude, longitude] = [float(latitude), float(longitude)]
                else:
                    [latitude, longitude] = getLocation.get_location(location)
                nature = remaining_line[1]
                incident_ori = remaining_line[2]
                # Getting WMO Code and side of town
                if(latitude and longitude):
                    weather_code = getWeather.get_weather_hour(latitude, longitude, date, hour)
                    if(weather_code != None):
                        weather_code = int(weather_code)
                    side_of_town = getLocation.get_direction(latitude, longitude)
                else:
                    weather_code = None
                    side_of_town = None
                output.append(weather_code) # Weather
                # Location Rank code goes here
                output.append(side_of_town) # Side of Town
                # Incident Rank code goes here
                output.append(nature) # Nature
                is_EMSSTAT = False
                if(incident_ori == "EMSSTAT"):
                    is_EMSSTAT = True
                output.append(is_EMSSTAT) # Incident ORI

            else:
                if(remaining_line[0].startswith('OK')):
                    output.append('') # Location
                    output.append('') # Weather
                    output.append('') # Side of Town
                    output.append('') # Nature
                    output.append(remaining_line[0]) # Incident ORI
        
        if(not (len(output) < 5)):
            row_list.append(output)
    return row_list

# Function to create normanpd.db
def createdb():

    database_path = os.path.join('normanpd.db')
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Drop the table if it already exists
    drop_table = ''' DROP TABLE IF EXISTS incidents; '''

    # Query to create a table
    create_table = '''
        CREATE TABLE  incidents (
            day INTEGER,
            incident_time INTEGER,
            time TEXT,
            incident_number TEXT,
            incident_location TEXT,
            weather_code INTEGER,
            side_of_town TEXT,
            nature TEXT,
            incident_ori TEXT
        );
    '''
    cursor.execute(drop_table)
    cursor.execute(create_table)
    connection.commit()
    connection.close()

# Function to populate data
def populatedb(incidents):

    database_path = os.path.join('normanpd.db')
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    for row in incidents:
        cursor.execute('INSERT INTO incidents (day, incident_time, time, incident_number, incident_location, weather_code, side_of_town, nature, incident_ori) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', row)
    connection.commit()
    connection.close()

# Function to get nature count
def status():
    database_path = os.path.join('normanpd.db')
    connection = sqlite3.connect(database_path)
    query = "SELECT * FROM incidents;"
    df = pd.read_sql_query(query, connection)
    connection.close()
    csv_file_path = 'output.csv'
    df = fd.rankData(df, 'incident_location', 'location_rank')
    df = fd.rankData(df, 'nature', 'incident_rank')
    df['incident_ori'] = df.groupby(['time', 'incident_location'])['incident_ori'].transform(lambda x: '1' if (x == '1').any() else '0')
    df['incident_ori'] = df['incident_ori'].map(fd.convert_to_boolean)
    columns_to_remove = ['time', 'incident_number', 'incident_location']
    df = df.drop(columns=columns_to_remove)
    new_columns = {
        'day': 'Day of the Week', 
        'incident_time': 'Time of Day', 
        'weather_code': 'Weather', 
        'side_of_town': 'Side of Town', 
        'nature': 'Nature', 
        'incident_ori': 'EMSSTAT',
        'location_rank': 'Location Rank',
        'incident_rank': 'Incident Rank'
        }
    df = df.rename(columns=new_columns)
    df = df[['Day of the Week', 'Time of Day', 'Weather', 'Location Rank', 'Side of Town', 'Incident Rank', 'Nature', 'EMSSTAT']]
    df.to_csv(csv_file_path, index=False)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    df.to_csv(sys.stdout, sep='\t', index=False)
    return df
