#!/usr/bin/env python3


import csv
import datetime
import requests


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"
GET_DATA = {}
def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()
    # return year + "-" + month + "=" + "day"
    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    
    if not GET_DATA:
        data = get_file_lines(FILE_URL)
        reader = csv.reader(data[1:])
        for row in reader: 
            row_date = row[3]
            name = row[0] + ' ' + row[1]
            if GET_DATA.get(row_date, []):
                GET_DATA[row_date].append(name)
            else:
                GET_DATA[row_date] = [name]


    fetch_data = str(start_date)
    fetch_data = fetch_data.split()[0]
    return start_date, GET_DATA.get(fetch_data)

def list_newer(start_date):
    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(start_date)
        if employees:
            print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))
        # print("The data of {} is {}".format(start_date, employees))
        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()
