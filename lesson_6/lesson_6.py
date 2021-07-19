#
#
# def get_talk(type_="shout"):
#     def shout(word="да"):
#         return word.capitalize() + "!"
#
#     def whisper(word="да"):
#         return word.lower() + "..."
#
#     if type_ == "shout":
#         return shout
#     else:
#         return whisper
#
#
# talk = get_talk()
# print(talk)
# print(talk())
# print(get_talk("whisper")())

# def my_shiny_new_decorator(a_function_to_decorate):
#     def the_wrapper_around_the_original_function():
#         print("Я - код, который отработает до вызова функции")
#         a_function_to_decorate()
#         print("А я - код, срабатывающий после")
#     return the_wrapper_around_the_original_function
#
#
# @my_shiny_new_decorator
# def a_stand_alone_function():
#     print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?..")
#
#
# a_stand_alone_function()

# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):
#         print("Смотри, что я получил:", arg1, arg2)
#         function_to_decorate(arg1, arg2)
#
#     return a_wrapper_accepting_arguments
#
#
# @a_decorator_passing_arguments
# def print_full_name(first_name, last_name):
#     print("Меня зовут", first_name, last_name)
#
#
# print_full_name("Питер", "Венкман")


# def method_friendly_decorator(method_to_decorate):
#     def wrapper(self, lie):
#         lie = lie - 3
#         return method_to_decorate(self, lie)
#     return wrapper
#
#
# class Lucy(object):
#     def __init__(self):
#         self.age = 32
#
#     @method_friendly_decorator
#     def say_your_age(self, lie):
#         print("Мне %s, а ты бы сколько дал?" % (self.age + lie))
#
#
# lucy_ = Lucy()
# lucy_.say_your_age(-3)

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print(f'Передали ли мне что-нибудь?:')
        print(args)
        print(kwargs)
        function_to_decorate(*args, **kwargs)

    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print(f'Python is cool, no argument here.')


# function_with_no_argument()


@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


# function_with_arguments(1, 2, 3)


@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Почему нет?"):
    print(f'Любят ли {a}, {b} и {c} утконосов? {platypus}')


# function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")


class Mary(object):
    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def say_your_age(self, lie=-3):
        print(f'Мне {self.age + lie}, а ты бы сколько дал?')


# m = Mary()
# m.say_your_age()

# ######################
# Decorator in decorator
# ######################

def decorator_with_args(decorator_to_enhance):
    """
    Эта функция задумывается КАК декоратор и ДЛЯ декораторов.
    Она должна декорировать другую функцию, которая должна быть декоратором.
    Лучше выпейте чашку кофе.
    Она даёт возможность любому декоратору принимать произвольные аргументы,
    избавляя Вас от головной боли о том, как же это делается, каждый раз, когда этот
    функционал необходим.
    """

    # Мы используем тот же трюк, который мы использовали для передачи аргументов:
    def decorator_maker(*args, **kwargs):
        # создадим на лету декоратор, который принимает как аргумент только
        # функцию, но сохраняет все аргументы, переданные своему "создателю"
        def decorator_wrapper(func):
            # Мы возвращаем то, что вернёт нам изначальный декоратор, который,
            # в свою очередь
            # ПРОСТО ФУНКЦИЯ (возвращающая функцию).
            # Единственная ловушка в том, что этот декоратор должен быть именно такого
            # decorator(func, *args, **kwargs)
            # вида, иначе ничего не сработает
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


# Мы создаём функцию, которую будем использовать как декоратор и декорируем её :-)
# Не стоит забывать, что она должна иметь вид "decorator(func, *args, **kwargs)"
@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    def wrapper(function_arg1, function_arg2):
        print("Мне тут передали...:", args, kwargs)
        return func(function_arg1, function_arg2)
    return wrapper


# Теперь декорируем любую нужную функцию нашим новеньким, ещё блестящим декоратором:

@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print("Привет", function_arg1, function_arg2)


# decorated_function("Вселенная и", "всё прочее")

def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    import time

    def wrapper(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print(func.__name__, time.time() - t)
        return res

    return wrapper


def logging(func):
    """
    Декоратор, логирующий работу кода.
    (хорошо, он просто выводит вызовы, но тут могло быть и логирование!)
    """

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res

    return wrapper


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper


@benchmark
@logging
@counter
def reverse_string(string):
    return str(reversed(string))


print(reverse_string("А роза упала на лапу Азора"))
print(reverse_string('''A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, 
maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (
or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, 
a canal: Panama!'''))
