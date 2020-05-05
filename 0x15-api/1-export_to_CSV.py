#!/usr/bin/python3
""" Script to export data in the CSV format."""

import csv
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
    user_name = content.get('username')
    tasks = len(info)
    count = 0
    for comp in info:
        finished = comp.get('completed')
        if finished:
            count += 1
    with open('{}.csv'.format(id), 'w') as f:
        fields = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in info:
            uid = task.get('userId')
            complet = task.get('completed')
            title = task.get('title')
            f_csv = [uid, user_name, complet, title]
            fields.writerow(f_csv)
