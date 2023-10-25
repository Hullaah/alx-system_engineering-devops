#!/usr/bin/python3
"""A Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress and then
export data in the CSV format"""
import json
import requests
import sys


def main():
    payload = {"userId": sys.argv[1]}
    req1 = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}")
    req2 = requests.get(
        f"https://jsonplaceholder.typicode.com/todos", params=payload)
    employee = req1.json()
    employee_todos = req2.json()
    with open(f"{employee['id']}.json", "w") as file:
        x = {f"{employee['id']}": []}
        for employee_todo in employee_todos:
            x[f"{employee['id']}"].append({
                "task": employee_todo["title"],
                "completed": employee_todo["completed"],
                "username": employee["name"],
            })
        json.dump(x, file)


if __name__ == "__main__":
    main()
