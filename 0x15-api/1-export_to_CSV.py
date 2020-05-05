#!/usr/bin/python3
""" Script to export data in the CSV format."""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    tmp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        id)).json()
    temp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            id)).json()

    name = tmp.get('username')
    info = []
    for tasks in temp:
        data = {}
        data['USER_ID'] = str(tasks.get('userId'))
        data['USERNAME'] = str(name)
        data['TASK_COMPLETED_STATUS'] = str(tasks.get('completed'))
        data['TASK_TITLE'] = str(tasks.get('title'))
        info.append(data)
    header = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    with open('{}.csv'.format(id), 'w') as fcsv:
        f_csv = csv.DictWriter(fcsv, fieldnames=header, quoting=csv.QUOTE_ALL)
        f_csv.writerows(info)
