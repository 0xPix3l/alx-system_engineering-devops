#!/usr/bin/python3
"""
return info about info from a given ID
"""

import requests
import sys

if __name__ == "__main__":
    user_ID = sys.argv[1]
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_ID}')

    name = user.json().get('name')

    todos = requests.get(f'https://jsonplaceholder.typicode.com/todos')

    tasks = 0
    done = 0

    for task in todos.json():
        if task.get('userId') == int(user_ID):
            tasks += 1
            if task.get('completed'):
                done += 1

    print(f"Employee {name} is done with tasks({done}/{tasks}):")

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(user_ID) and task.get('completed')]))
