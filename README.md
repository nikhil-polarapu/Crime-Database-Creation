# cis6930sp24 -- Assignment2

Name: Nikhil Polarapu \
UFID: 16049519 \
Email: spolarapu@ufl.edu

# Assignment Description

In this assignment we write a program that goes through the pdf file of Norman Police Department that has the incidents, arrests and other activities. The program reads the tabular data, cleans it and converts it into a list-of-lists, each list representing a row of the table. Using this data we create an sqlite database with a table called incidents that has the following columns.

In assignment 0 we wrote a progrma to extract incident summary data from Norman police department website. This data has the following columns 

- Date/Time
- Incident Number
- Location
- Nature
- Incident ORI

In this assignment we use the above data gathered in assignment 0 to gain insights in the form of the following columns

- **Day of Week**: The day of week is a numeric value in the range 1-7. Where 1 corresponds to Sunday and 7 corresonds of Saturday.
- **Time of Day**: The time of data is a numeric code from 0 to 24 describing the hour of the incident.
- **Weather**: Determine the weather at the time and location of the incident. The weather is determined by the WMO CODE.
- **Location Rank**: An integer ranking of the frequency of locations with ties preserved.
- **Side of Town**: The side of town with respect to the center of town 35.220833, -97.443611.
- **Incident Rank**: An integer ranking of the frequency of natures with ties preserved.
- **Nature**: Nature of the incident.
- **EMSSTAT**: This is true if the Incident ORI was EMSSTAT or if the subsequent record or two contain an EMSSTAT at the same time and locaton.

This data will be printed to stdout in tab-separated form.

# How to install

- curl https://pyenv.run | bash
- pyenv install 3.11
- pyenv global 3.11
- pip install pipenv
- pipenv install pypdf
- pipenv install pytest
- pipenv install pandas
- pipenv install geopy
- pipenv install openmeteo_requests
- pipenv install requests_cache
- pipenv install retry_requests
- pipenv install requests

## How to run

- pipenv run python assignment2.py --urls files.csv2024-02-01_daily_incident_summary.pdf
- pipenv run python -m pytest

![DE Assignment2 Demo](/DE%20Assignment2%20Demo.gif)


## Functions

#### assignment2.py \

- main( ) - This function takes in the URLs extracted from the files.csv file and runs the functions in assignment0.py to get the desired output.

#### assignment2_helper.py \

- fetchincidents( ) - This function takes the URL as parameter, extracts the data in the page and returns this data in the byte form.

- extractincidents( ) - This function takes in the result of the fetchincidents( ) function as the parameter, extracts the incident data present in the table. It then uses several functions that we will further discuss convert it to the desired dataset and returns it as a list-of-lists.

- createdb( ) - This function executes an SQL query that checks if a table called incidents exists in the normanpd.db database, deletes it if it already exists and creates a new one by executing a different query. This function does not take any parameters and does not return anything.

- populatedb( ) - This function takes in the list-of-lists returned by extractincidents( ) function as parameters. It executes an SQL query that connects to the normanpd.db database, inserts the list-of-lists data (each list as a row) into the incidents table. This function does not return anything.

- status( ) - This function executes an SQL query that extracts all the rows from the database. It then performs some operations to convert this inital dataset into the desired form. This function does not return anything, it justs prints the data to stdout.

#### format_data.py \

- dayOfWeek( ) - This function takes in the date and returns the day of the week.

- hourOfDay( ) - This function takes in the time and returns the hour of the day.

- changeDateFormat( ) - This function takes in the date and changes it to YYYY-MM-DD format, which is the only format accepted by the Open-Meteo weather API. It returns this modified weather format.

- rankData( ) - This function in the dataframe, column name and the new column name. It ranks the values in the specified column of the dataframe and adds them as a new column with the new column name to the dataframe.

#### get_location.py \

- get_location( ) - This function takes in the address and returns the latitude and the longitude of the address.

- get_direction( ) - This function takes in the latitude and the longitude, and returns the direction of this location with respect to the center of the town.

- is_location_format( ) - Some addresses in the data are already given as coordinates. This function takes in the location and True if the location is given as coordinates, and False if the location is given as address.

#### get_weather.py \

- get_weather_code( ) - This function takes in the latitude, the longitude and the date as arguments and returns the weather data at that location on that day. It uses the Open-Meteo API.

- get_weather_hour( ) - This function takes the data returned by get_weather_code() function and the hour as inputs and returns the weather code on that particular hour.

## Database Development

- **Query to create the table**
  cursor.execute(CREATE TABLE  incidents (day INTEGER, incident_time INTEGER, time TEXT, incident_number TEXT, incident_location TEXT, weather_code INTEGER, side_of_town TEXT, nature TEXT, incident_ori TEXT)\;)

- **Query to insert data into the table**
    cursor.execute('INSERT INTO incidents (day, incident_time, time, incident_number, incident_location, weather_code, side_of_town, nature, incident_ori) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', row)


- **Query to select the data**
  cursor.execute('SELECT * FROM incidents;')

## Bugs and Assumptions

The following assumptions were made:
  
- There are always 5 columns in the table.
- There date/time and incident number columns are always non-empty.
- The column names and page heading are always the same and they never change.

If any page does not follow the above-mentioned assumptions then bugs related to these assumptions may be encountered.

## Testcase Discussion

- test_fetchincidents_output( ) - Testcase to check if data is fetched properly from the URL.
- test_fetchincidents_invalid_url( ) - Testcase to check if error occurs when wrong URL is given.
- test_extractincidents( ) - Testcase to check if correct incidents are extracted
- test_createdb_check_file( ) - Testcase to check if the database file is created.
- test_populatedb_check_data( ) - Testcase to check if a single row is populated correctly.
- test_populate_db_multiple_rows( ) - Testcase to check if multiple rows are populated correctly.
- test_status_empty_nature( ) - Testcase to check if empty nature count is displayed.
- test_status( ) - Testcase to check if correct dataframe is created.
- test_check_day( ) - Testcase to check if correct day is extracted.
- test_check_hour( ) - Testcase to check if correct hour is extracted.
- test_check_change_format( ) - Testcase to check if correct hour is extracted.
- test_check_ranking( ) - Testcase to check if ranking is done correctly.
- test_location( ) - Testcase to check if correct coordinates are returned.
- test_direction( ) - Testcase to check if correct direction is returned.
- test_weather_code( ) - Testcase to check if correct weather code is returned.
