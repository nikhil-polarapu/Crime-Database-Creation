import src.assignment2_helper as assignment2
import pytest
import os
import sqlite3

# Testcase to check if a single row is populated correctly
def test_populatedb_check_data():
    db = assignment2.createdb()
    incidents = [[5, 0, '0:10', '2024-00002259', '3300 HEALTHPLEX PKWY', 1, 'NW', 'Transfer/Interfacility', True]]
    assignment2.populatedb(incidents)
    database_path = os.path.join('normanpd.db')
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute('SELECT nature FROM incidents')
    for row in cursor.fetchall():
        nature = row[0]
        assert nature == incidents[0][7]
    connection.commit()
    connection.close()

# Testcase to check if multiple rows are populated correctly
def test_populate_db_multiple_rows():
    db = assignment2.createdb()
    incidents = [[5, 0, '0:10', '2024-00002259', '3300 HEALTHPLEX PKWY', 1, 'NW', 'Transfer/Interfacility', True], [5, 0, '0:14', '2024-00007318', '1152 W LINDSEY ST', 1, 'SW', 'Traffic Stop', False]]
    assignment2.populatedb(incidents)
    database_path = os.path.join('normanpd.db')
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute('SELECT nature FROM incidents')
    nature = []
    for row in cursor.fetchall():
        i = 0
        nature.append(row[0])
    for i in range(len(nature)):
        assert nature[i] == incidents[i][7]
    connection.commit()
    connection.close()