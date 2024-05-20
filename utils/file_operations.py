"""
This file is to define some file operations like reading from file and writing into file
"""


def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
