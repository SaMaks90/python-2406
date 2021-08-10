# Homework:
class CustomIterators:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __next__(self):
        self.index += 1
        if self.index <= len(self.sequence):
            return self.sequence[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


# 1. Create an iterator that returns values from the given sequence circularly  (for
# example: [1, 2,3 ] -> 1, 2, 3, 1, 2, 3, 1, 2, etc.)
class CircularlyIterators(CustomIterators):
    def __next__(self):
        if self.index == len(self.sequence):
            self.index = 0
        result = self.sequence[self.index]
        self.index += 1
        return result


# 2. Create an iterator that generates even numbers from the given range
class EvenIterators(CustomIterators):
    def __iter__(self):
        result = []
        for elem_iter in self.sequence:
            if elem_iter % 2 == 0:
                result.append(elem_iter)
        self.sequence = result
        return self


# 3. Create an iterator that iterates elements from the last element of the sequence to
# the first. Raise StopIteration exception when elements end.
class LstToFirstIterators(CustomIterators):
    def __iter__(self):
        result = self.sequence[::-1]
        self.sequence = result
        return self


# 4. Create a decorator that can handle any kind of exception. The decorator should
# contains a parameter “debug=True” that responsible for printing exception traceback.
# If debug=False - just print exception name
def debug_decorator(debug=True):
    def print_debug_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as error:
                if debug:
                    print(error)
                else:
                    print(error.__class__.__name__)
        return wrapper
    return print_debug_error
