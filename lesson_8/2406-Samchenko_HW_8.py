# Homework
# Create a library that allows us to manipulate with files
# The library should have the next functionality:
# find all files by name in the given directory. By default should look for files in
# the current working directory. Has to be recursive (it should look for files in
# nested directories).
# Function interface:
# def find(filename, directory='.', recursive=True): -> [<list of files match the
# pattern 'filename'>]
# delete files by given name. (Tip: use function find() for searching files to delete)
# move files from one directory to another. If target directory doesn't exist you
# should create it.
# User functions should be accessible via __init__.py (so you can import it from your
# module directly, without importing from submodule)
# As result, you should have the next module structure (or simmilar):
# <your_module_name>
#        |-  __init__.py
#        |-  search_tools.py
#        |-  delete_tools.py
#        |-  etc...

from manipulation_with_file import delete_files, find, move_files

print(find('test', directory='./test'))
print(find('test', recursive=True))
move_files('test.py', './test2/test3/test4', './test')
delete_files('test.py', recursive=True)

