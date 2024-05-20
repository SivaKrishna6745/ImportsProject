"""
This file is to import file operations and utilize them
"""

from utils import file_operations

file_operations.save_to_file('Rolf', 'data.txt')
file_content = file_operations.read_file('data.txt')
print(file_content)  # Rolf
