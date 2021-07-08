

def function(name):
    print(f'Hello {name}.')


function('Maks')


def calculus(a, b, power=2):
    print(f'Calculating for: {a}, {b}')
    result = a**power + b**power
    print(f'{a}^{power} + {b}^{power} = {result}')

    return result


def calculus_v2(*args, verbose=True, **kwargs):
    print(f'Args: {type(args)} {args}')
    print(f'Kwargs: {type(kwargs)} {kwargs}')
    sum_func = 0
    for el in args:
        sum_func += el**kwargs['power']
    if verbose:
        return sum_func
    return sum_func, sum_func // 2


res_v2_1 = calculus_v2(1, 2, 3, 6, 10, 20, power=3, verbose=False)
res_v2_2 = calculus_v2(1, 2, 3, 6, 10, 20, power=3)
print(type(res_v2_1))
print(type(res_v2_2))

res = calculus(1, 5)
res2 = calculus(4, 6, 3)
print(f'{res2} - {res} = {res2 - res}')

# Mutable type (change object):
print(f'Mutable type:')
# - list
a = (12, 13, 14)
b = (1, 2, 3)
id_first = id(a)
a += b
id_second = id(a)
print(f'1. List type:\nFirst id: {id_first};\nSecond if: {id_second}')

# - set
a = set({12, 13})
b = set({1, 2, 3, 5})
id_first = id(a)
a.update(b)
print(a)
id_second = id(a)
print(f'2. Set type:\nFirst id: {id_first};\nSecond if: {id_second}')

# - dict
# a = {
#     'first': 1
# }
# id_first = id(a)
# b = {
#     'second': 12
# }
#
# a.update(b)
# print(a)
# id_second = id(a)
# print(f'2. Dict type:\nFirst id: {id_first};\nSecond if: {id_second}')
