import os
from .search_tools import find


def delete_files(filename, directory='.', recursive=False):
    list_files = find(filename, directory, recursive)
    for file in list_files:
        os.remove(file)
        print(f'File deleted: {file}')
