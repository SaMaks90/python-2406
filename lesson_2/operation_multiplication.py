for i in range(1, 10):
    row = ''
    for j in range(1, 10):
        row += f'{i * j:3}'
    else:
        print(row)