import os


def find(filename, directory='.', recursive=False):
    if directory == '.':
        directory = os.path.abspath('.')
    list_files = []
    for file in os.listdir(directory):
        path_file = f'{directory}/{file}'
        if os.path.isfile(path_file) \
                and file[:file.find('.')] == filename:
            list_files.append(path_file)
        if recursive and os.path.isdir(path_file):
            new_list_files = find(filename, path_file, recursive)
            if new_list_files:
                for new_file in new_list_files:
                    list_files.append(new_file)
    return list_files
