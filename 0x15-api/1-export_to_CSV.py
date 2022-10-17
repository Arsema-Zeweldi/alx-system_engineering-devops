#!/usr/bin/python3
"""
export data in the CSV format
"""
import csv
import requests
from sys import argv


def csv_format(uid):
    """uses uid"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(uid)
    tasks = requests.get(url, verify=False).json()
    with open("{}.csv".format(uid), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([int(uid), user.get('username'),
                             task.get('completed'),
                             task.get('title')])

if __name__ == "__main__":
    csv_format(argv[1])
