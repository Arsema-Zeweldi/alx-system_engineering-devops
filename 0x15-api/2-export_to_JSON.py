#!/usr/bin/python3
"""
export data in the JSON format
"""

import json
import requests
from sys import argv


def json_format(uid):
    """user uid"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(uid)
    tasks = requests.get(url, verify=False).json()
    name = user.get('username')
    task = [{"task": task.get("title"),
             "username": name,
             "completed": task.get("completed")} for task in tasks]
    JSON = {}
    JSON[uid] = task
    with open("{}.json".format(uid), 'w') as filejs:
        json.dump(JSON, filejs)


if __name__ == "__main__":
    json_format(argv[1])
