#!/usr/bin/python3
"""A Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress and then
export data in the CSV format"""
import json
import requests
import sys


def main():
    req = requests.get(
        f"https://jsonplaceholder.typicode.com/users/")
    employees = req.json()
    with open("todo_all_employees.json", "w") as file:
        json_file_content = {}
        for employee in employees:
            payload = {"userId": employee["id"]}
            req = requests.get(
                f"https://jsonplaceholder.typicode.com/todos", params=payload)
            employee_todos = req.json()
            for employee_todo in employee_todos:
                x = {
                    "task": employee_todo["title"],
                    "completed": employee_todo["completed"],
                    "username": employee["name"],
                }
                if f"{employee['id']}" in json_file_content:
                    json_file_content[f"{employee['id']}"].append(x)
                else:
                    json_file_content[f"{employee['id']}"] = [x]
        json.dump(json_file_content, file)


if __name__ == "__main__":
    main()
