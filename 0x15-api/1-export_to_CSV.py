#!/usr/bin/python3
"""
export data in the CSV format
"""
import csv
import requests
from sys import argv

def csv_format(employeeid):
    """uses employee id"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employeeid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employeeid)
    tasks = requests.get(url, verify=False).json()
    with open("{}.csv".format(employeeid), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([int(employeeid), user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])

if __name__ == "__main__":
    csv_format(argv[1])
