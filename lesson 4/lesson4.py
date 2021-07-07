

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
