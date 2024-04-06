from datetime import datetime
import pandas as pd

def dayOfWeek(date):
    day = (datetime.strptime(date, '%m/%d/%Y').weekday()+2)
    if(day == 7):
        return day
    else:
        return day%7

def hourOfDay(time):
    return datetime.strptime(time, '%H:%M').hour

def changeDateFormat(date):
    date = datetime.strptime(date, '%m/%d/%Y')
    return date.strftime('%Y-%m-%d')

def rankData(df, column, to_name):
    counts = df[column].value_counts()
    sorted_values = counts.sort_values(ascending=False).index
    rankings = {}
    rank = 1
    for location in sorted_values:
        count = counts[location]
        if count not in rankings:
            rankings[count] = rank
        rank += 1
    df[to_name] = df[column].map(counts).map(rankings)
    return df

def convert_to_boolean(value):
    if value == '1':
        return 1
    elif value == '0':
        return 0
    else:
        return 0