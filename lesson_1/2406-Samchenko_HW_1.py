#!/usr/bin/env python
# coding: utf-8
# Task 1: 
# Create a script that can calculate squares of the next geometric figures:
# circle, rectangle triangle(with an angle 90 degrees), rectangle
r = 10      # here you should set the radius of the circle
a = 15      # here you should set the first side of the rectangle
b = 12      # here you should set the second side of the rectangle

circle_square = 3.14 * (r ** 2)
# here you should define a formula of the circle
rec_triangle_square = (a * b) / 2
# here you should define a formula of the rectangle triangle
rectangle_square = a * b
# here you should define a formula of the rectangle

print(f'Circle: r={r}, S={circle_square}')
print(f'Rectangle triangle: a={a}, b={b}, S={rec_triangle_square}')
print(f'Rectangle: a={a}, b={b}, S={rectangle_square}')
