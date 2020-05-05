#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    tmp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        id))
    temp = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id))

    content = tmp.json()
    info = temp.json()
    name = content.get('name')
    tasks = len(info)
    count = 0
    for comp in info:
        finished = comp.get('completed')
        if finished:
            count += 1
    print('Employee {} is done with tasks({}/{}):'.format(name, count, tasks))
    for data in info:
        completed = data.get('completed')
        if completed:
            title = data.get('title')
            print("\t {}".format(title))
