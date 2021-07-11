# Task 1.
# Create a class Point that takes two arguments as input Point(x, y)
# Create a method that describes an object (preferably use __str__())
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point x: {self.x}\n Point y: {self.y}'

# Task 2
# Create a class Figure that takes any count of Point() objects as input. Create a
# methods perimeter() and square() that return nothing for this class


class Figure:

    def __init__(self, *args):
        self.points_args = args

    def __add__(self, figure):
        return self.square() + figure.square()

    def __sub__(self, figure):
        return self.square() - figure.square()

    def perimeter(self):
        return 0

    def square(self):
        return 0

    def get_sides(self):
        list_ = []
        for elem in self.points_args:
            list_.append(elem.x)
            list_.append(elem.y)
        a = math.sqrt(((list_[2] - list_[0]) ** 2) + ((list_[3] - list_[1]) ** 2))
        b = math.sqrt(((list_[4] - list_[0]) ** 2) + ((list_[5] - list_[1]) ** 2))
        c = math.sqrt(((list_[4] - list_[2]) ** 2) + ((list_[5] - list_[3]) ** 2))

        return [a, b, c]

# Task 3
# Create classes Triangle, Rectangle and Circle that inherit from Figure class.
# Try to use your imagination to define class constructors :)
# Overwrite methods square() and perimeter()


class Triangle(Figure):

    def perimeter(self):
        sides = self.get_sides()
        perimeter_ = 0
        for elem in sides[:3]:
            perimeter_ += elem

        return perimeter_

    def square(self):
        sides = self.get_sides()
        perimeter_ = 0
        for elem in sides[:3]:
            perimeter_ += elem
        half_per = perimeter_ / 2
        square_ = math.sqrt(half_per * (half_per - sides[0]) * (half_per - sides[1]) *
                            (half_per - sides[2]))

        return square_


class Rectangle(Figure):

    def perimeter(self):
        sides = self.get_sides()
        sum_sides = 0
        for elem in sides[:2]:
            sum_sides += elem
        perimeter_ = 2 * sum_sides

        return perimeter_

    def square(self):
        sides = self.get_sides()
        square_ = 1
        for elem in sides[:2]:
            square_ *= elem

        return square_


class Circle(Figure):

    def perimeter(self):
        r = self.get_sides()[0]
        perimeter_ = 2 * 3.14 * r

        return perimeter_

    def square(self):
        r = self.get_sides()[0]
        square_ = 3.14 * (r ** 2)

        return square_

# Bonus task:
# Implement method that allows to summarize and sub figures between (via “+”
# and “-“ operator)
