# Homework 4
# Exercise 1: Create a function that can accept two arguments name and age and print
# its value


def create_sentences(name, age):
    print(f'My name is {name}, I\'m {age} years old.')


create_sentences('Maxim', 31)

# Exercise 2: implement a function that returns the largest and the smallest items from
# the given list. (Don’t use max() and min() function, find values by yourself:) )
# Function should return two values simultaneously


def find_min_max_number(numbers_list):
    min_num = None
    max_num = None

    for elem in numbers_list:
        if min_num is None and max_num is None:
            min_num = elem
            max_num = elem
        elif elem > max_num:
            max_num = elem
        elif elem < min_num:
            min_num = elem

    return min_num, max_num


print(find_min_max_number([12, 13, 25, 40, -2, -4, 0]))

# Exercise 3: implement a function that calls previous function (from ex.2) inside
# itself and generates a list of values from min to max
# For example:
# Min = -3
# Max = 34
# Generated list: [-3, -2, -1, ….., 32, 33, 34]


def generate_list(numbers_list):
    gen_list = []
    num_min, num_max = find_min_max_number(numbers_list)

    for num in range(num_min, num_max + 1):
        gen_list.append(num)

    return gen_list


print(generate_list([34, -3]))

# Exercise 4
# Let's use functions to calculate your trip's costs:
# Define a function called hotel_cost with one argument nights as input. The hotel costs
# $140 per night. So, the function hotel_cost should return 140 * nights. Define a
# function called plane_ride_cost that takes a string, city, as input. The function
# should return a different price depending on the location, similar to the code
# example above. Below are
# the valid destinations and their corresponding round-trip prices."Charlotte": 183
# "Tampa": 220
# "Pittsburgh": 222
# "Los Angeles": 475
# -Below your existing code, define a function called rental_car_cost with an argument
# called days. Calculate the cost of renting the car: Every day you rent the car costs
# $40.(cost=40*days) if you rent the car for 7 or more days, you get $50 off your
# total(cost-=50). Alternatively (elif), if you rent the car for 3 or more days,
# you get $20 off your total. You cannot get both of the above discounts. Return that
# cost. -Then, define a function called trip_cost that takes two arguments, city and
# days. Like the example above, have your function return the sum of calling the
# rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city) functions.
# Modify your trip_cost function definion. Add a third argument, spending_money. Modify
# what the trip_cost function does. Add the variable `spending_money to the sum that it
# returns.


def hotel_cost(city, quantity_night):
    return plane_ride_cost(city) * quantity_night


def plane_ride_cost(city):
    cities = {
        'Charlotte': 183,
        'Pittsburgh': 222,
        'Los Angeles': 475
    }

    return cities[city]


def rental_car_cost(day_rental):
    discount = 0
    if day_rental >= 7:
        discount = 50
    elif 3 >= day_rental < 7:
        discount = 20

    return (day_rental * 40) - discount


def trip_cost(city, days, spending_money=0):
    return rental_car_cost(days) + hotel_cost(city, days) + spending_money


print(f'Trip in Charlotte city on the 7 days with spendi'
      f'ng money 200$: {trip_cost("Charlotte", 3, 200)}$')
print(f'Trip in Pittsburgh city on the 7 days: {trip_cost("Pittsburgh", 7)}$')
print(f'Trip in Los Angeles city on the 7 days with spendi'
      f'ng money 800$: {trip_cost("Los Angeles", 10, 800)}$')
