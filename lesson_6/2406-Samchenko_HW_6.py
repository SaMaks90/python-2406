import time

# Task 1:
# Create a decorator that shows a time of execution of any function


def lead_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Function execution time: {end_time - start_time} s')
        return result
    return wrapper

# Task 2:def function(arg1, arg2):
#         time.sleep(10)
#         return arg1  arg2
# Create a decorator that store result of function execution in cache
# It means if you’ve passed this parameters to the function you shouldn’t run the
# function again bur return result. As parameter, you should add cache_size.
# To show everything works properly use your decorator from the first taskCreate a
# decorator that shows a time of execution of any function


def cache_save(cache_size=8):
    def cache_save_repeat(func):
        cache = dict()

        def wrapper(*args, **kwargs):
            print(f'Run function with params: {args}')
            if args not in cache:
                print(f'Params {args} don\'t find in cache!')
                if cache.__len__() == cache_size:
                    print(f'Cache full..... Cleaning!')
                    for key in cache.keys():
                        del cache[key]
                        break
                cache[args] = func(*args, **kwargs)
                print(f'Params added in cache!')
            else:
                print(f'Params {args} find in cache!')
            print(cache)
            return cache[args]
        return wrapper
    return cache_save_repeat


@cache_save(2)
@lead_time
def function(arg1, arg2):
    time.sleep(2)
    return arg1, arg2


function(112, 5)
function(1, 5)
function(10, 5)
function(2, 5)
function(112, 5)
function(1, 5)
