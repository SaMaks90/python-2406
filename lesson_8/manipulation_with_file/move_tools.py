from os import replace, makedirs, path


def move_files(filename, went_directory, from_directory='.'):
    if not path.isdir(went_directory):
        makedirs(went_directory)
    replace(path.join(from_directory, filename), path.join(went_directory, filename))
    print(f'File \'{filename}\' move with {from_directory} in {went_directory}')
