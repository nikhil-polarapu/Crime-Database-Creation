from datetime import datetime

def dayOfWeek(date):
    return datetime.strptime(date, '%m/%d/%Y').weekday()

def hourOfDay(time):
    return datetime.strptime(time, '%H:%M').hour

def changeDateFormat(date):
    date = datetime.strptime(date, '%m/%d/%Y')
    return date.strftime('%Y-%m-%d')