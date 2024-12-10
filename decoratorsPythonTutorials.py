#!/usr/bin/env python3

#thanks to @patloeber's youtube channel

import functools

# a decorator is a function that takes another function as argument and extends
# its behavior without modifying the original function

# functions and decorators in pythons are first class object
# which means they can be arguments and also be used a return values :)

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        # inside the wrapper execute the function
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def print_name():
    print('wakazoo')

# now print name has this new functionality with extended behavior :)

# the @ decorator name does the same as below by redefining print_name function!!!!
# print_name = start_end_decorator(print_name)

# now wakazoo got extened with start and end - wackaroonie
print_name()

@start_end_decorator
def add(x, y):
    return x + y

# does not work as the wrapper did not have any args and kwargs to begin with
sumxy = add(5, 10)
print(sumxy)

print(help(add))
print(add.__name__)
