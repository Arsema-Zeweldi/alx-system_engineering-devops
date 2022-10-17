#!/usr/bin/python3
"""
export data in the JSON format
"""
import json
import requests
from sys import argv


def json_format(employeeid):
    """user employeeid"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employeeid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    .format(employeeid)
    tasks = requests.get(url, verify=False).json()
    name = user.get('username')
    task = [{"task": task.get("title"),
              "username": name,
              "completed": task.get("completed")} for task in tasks]
    JSON = {}
    JSON[employeeid] = task
    with open("{}.json".format(employeeid), 'w') as filejs:
        json.dump(JSON, filejs)


if __name__ == "__main__":
    json_format(argv[1])
