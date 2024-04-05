import src.assignment2_helper as assignment2
import pytest
import os

# Testcase to check if the database file is created
def test_createdb_check_file():
    assignment2.createdb()
    assert os.path.isfile("normanpd.db")
    incidents = [""]