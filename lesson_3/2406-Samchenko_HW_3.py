# Exercise 1: Concatenate two lists index-wise
# Input:
# list1 = [“M”, “na”, “i”, “Ke”]
# list2 = [“y”, “me”, “s”, “lly”]
# Output:
# [‘My’, ‘name’, ‘is’, ‘Kelly’]
list_first = ['M', 'na', 'i', 'Ke']
list_second = ['y', 'me', 's', 'lly']
list_concatenate = []

if len(list_first) > len(list_second):
    n = len(list_first)
else:
    n = len(list_second)

for i in range(n):
    values = ''
    if i < len(list_first):
        values += list_first[i]
    if i < len(list_second):
        values += list_second[i]
    list_concatenate.append(values)

print(f'List concatenate two list: {list_concatenate}')

# Exercise 2: Given a two Python list. Iterate both lists simultaneously such that list1 should display item
# in original order and list2 in reverse order
# Input:
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# Output:
# 10 400
# 20 300
# 30 200
# 40 100
list_first = [10, 20, 30, 40]
list_second = [100, 200, 300, 400]
n = len(list_first) - 1

for i in range(len(list_first)):
    print(f'{list_first[i]} {list_second[n]}')
    n -= i

# Exercise 3: Given a Python list, remove all occurrence of 20 from the list
# list1 = [5, 20, 15, 20, 25, 50, 20]
# Expected output:
# [5, 15, 25, 50]
list_ = [5, 20, 15, 20, 25, 50, 20]
for i in range(list_.count(20)):
    list_.remove(20)
print(list_)

# Exercise 4: Below are the two lists convert it into the dictionary
# keys = [‘Ten’, ‘Twenty’, ‘Thirty’]
# values = [10, 20, 30]
# Expected output:
# {‘Ten’: 10, ‘Twenty’: 20, ‘Thirty’: 30}
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict_ = {}
i = 0

for elem in keys:
    value = ''
    if i < len(values):
        value = values[i]
    dict_[elem] = value
    i += 1

print(f'Dictionary: {dict_}')

# Exercise 5: Check if a value 200 exists in a dictionary
# sampleDict = {‘a’: 100, ‘b’: 200, ‘c’: 300}
# Output:
# True
sample_dict = {
    'a': 100,
    'b': 200,
    'c': 300
}
check_value = False

for key in sample_dict:
    if sample_dict[key] == 200:
        check_value = True
        break

print(f'Check value 200 in dictionary: {check_value}')

# Exercise 6: Get the key of a minimum value from the following dictionary
# sampleDict = {
#   ‘Physics’: 82,
#   ‘Math’: 65,
#   ‘history’: 75
# }
# Expected output:
# Math
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'History': 75
}
key_minimum_value = ''
value_minimum_key = None

for key in sample_dict:
    if value_minimum_key is None \
            or sample_dict[key] < value_minimum_key:
        value_minimum_key = sample_dict[key]
        key_minimum_value = key

print(f'Dictionary minimum value in key: {key_minimum_value}')

# Exercise 7: Return a new set of identical items from a given two set
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
# {40, 50, 30}
set_first = {10, 20, 30, 40, 50}
set_second = {30, 40, 50, 60, 70}
print(set_first & set_second)

# Exercise 8: Return a set of all elements in either A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
# {20, 70, 10, 60}
set_first = {10, 20, 30, 40, 50}
set_second = {30, 40, 50, 60, 70}
print(set_first.symmetric_difference(set_second))

# Exercise 10: Check if two sets have any elements in common. If yes, display the common elements
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# Expected output:
# Two sets have items in common
# {10}
set_first = {10, 20, 30, 40, 50}
set_second = {60, 70, 80, 90, 10}
common_set = set_first & set_second
if common_set != set():
    print(common_set)

# Bonus task:
# Write a script that transforms given number from decimal to the binary format
# (Without using standard Python functions)
# 16 -> 10000
# 13 -> 1101
num_first = 16
num_second = 13
num_third = 129


def transform_binary_num(num):
    num_list = []

    while True:
        if (num // 2) == (num / 2):
            num_list.append('0')
        elif num == 1:
            num_list.append('1')
            break
        else:
            num_list.append('1')
        num //= 2

    binary = ''
    for element in num_list[::-1]:
        binary += element

    return binary


print(f'{num_first} -> {transform_binary_num(num_first)}')
print(f'{num_second} -> {transform_binary_num(num_second)}')
print(f'{num_third} -> {transform_binary_num(num_third)}')
