#!/usr/bin/python3
""" Script to export data in the JSON format."""

import csv
import json
import requests

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    user_info = users.json()
    n_users = len(user_info) + 1
    all_data = {}
    for id in range(1, n_users):
        tmp = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(id))
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
        data_dic = []
        data_list = {}
        for task in info:
            data_list = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": content.get('username')
                }
            data_dic.append(data_list)
        all_data[id] = data_dic

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_data, f)
