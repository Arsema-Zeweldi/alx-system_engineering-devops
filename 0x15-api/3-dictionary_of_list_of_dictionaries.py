#!/usr/bin/python3
"""
export data in the JSON format
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url, verify=False).json()
    all_user = {}
    data = {}
    for user in users:
        uid = user.get("id")
        data[uid] = []
        all_user[uid] = user.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    tasks = requests.get(url, verify=False).json()
    [data.get(task.get("userId")).append({"task": task.get("title"),
                                          "completed": task.get("completed"),
                                          "username": all_user.get(
                                                 task.get("userId"))})
     for task in tasks]
    with open("todo_all_employees.json", 'w') as jsf:
        json.dump(data, jsf)
