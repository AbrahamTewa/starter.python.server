import os
import psycopg2
import time

def task_hello():
    """hello"""

    def python_hello(targets):
        with open(targets[0], "a") as output:
            output.write("Python says Hello World!!!\n")

    return {
        'actions': [python_hello],
        'targets': ["hello.txt"],
        }


def task_python_version():
    return {
        'actions': [['python', '--version']]
        }
