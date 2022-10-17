#!/usr/bin/python3
"""
export data in the JSON format
"""
import json
import requests
from sys import argv


def json_format(uid):
    """no uid"""
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url + 'users').json()
    task = requests.get(url + 'todos').json()
    all_users = {}
    userData = {}
    for user in users:
        user_id = user.get("id")
        userData[user_id] = []
        all_users[user_id] = user.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    tasks = requests.get(url, verify=False).json()
    [userData.get(task.get("userId")).append({"task": task.get("title"),
                                              "completed": task.get("completed"),
                                              "username": undoc.get(task.get("userId"))})
    for task in tasks]
    with open("todo_all_employees.json", 'w') as jsf:
        json.dump(userData, jsf)


if __name__ == "__main__":
    json_format()
