# Task 1
# Write a python program to find the sum of all even numbers
# from 0 to 10
sum = 0
for i in range(10):
    if i % 2 == 0:
        sum += i
print(f'Task 1: Sum = {sum}')

# Task 2
# Write a python program to read four numbers (representing
# the four octets of an IP) and print the next five IP address
# Eg:
# Input:
# 192 168 255 252
ip_address = input('Enter IP address: ')
for i in range(5):
    new_ip_address = []
    num_class = ''
    for j in range(len(ip_address)):
        if ip_address[j] == ' ':
            new_ip_address.append(int(num_class))
            num_class = ''
        else:
            num_class += ip_address[j]
    new_ip_address.append(int(num_class))

    count = 1
    index = 3
    for elem_class in new_ip_address[::-1]:
        elem_class += 1
        if elem_class > 255:
            new_ip_address[index] = 0
            count = 1
        else:
            new_ip_address[index] = elem_class
            count = 0
            break
        index -= 1

    ip_address =  f'{new_ip_address[0]} {new_ip_address[1]} {new_ip_address[2]} {new_ip_address[3]}'
    print(ip_address)

# Task 3
# Write a python program to print the factorial of a given
# number
number = int(input('Enter the number "factorial": '))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
else:
    print(f'Task 2: Number = {number}, Factorial = {factorial}')

# Task 4
# Write a python program to print the first 10 numbers
# Fibonacci series
fib = [0, 1]
fib_series = int(input('Enter the number to display the first numbers of the Fibonache series: '))
for i in range(2, fib_series):
    fib.append(fib[i - 1] + fib[i - 2])
else:
    print(f'Fibonache series: {fib}')