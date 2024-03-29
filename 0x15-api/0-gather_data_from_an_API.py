#!/usr/bin/python3
"""A Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress"""
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
    completed_todos = [x for x in employee_todos if x["completed"]]
    total_todos = len(employee_todos)
    print(
        f"Employee {employee['name']} is done with tasks" +
        f"({len(completed_todos)}/{total_todos}):", end="\n\t ")
    print("\n\t ".join([x["title"] for x in completed_todos]))


if __name__ == "__main__":
    main()
