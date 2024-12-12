#!/usr/bin/env python3

# thanks to @patloeber's youtube channel

# this is awesome super power  - read it carefully and use wisely :)

import functools
from inspect import signature

# a decorator is a function that takes another function as argument and extends
# its behavior without modifying the original function

# functions and decorators in pythons are first class object
# which means they can be arguments and also be used a return values :)


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        # inside the wrapper execute the function
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper


@start_end_decorator
def print_name():
    print("wakazoo")


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


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ",".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__!r}({signature})")
        result = func(*args, **kwargs)
        return result

    return wrapper


# decorators exectued in the order they are listed
# overlay a debug decorator - this is awesome!!! Love it!!!
@debug
# repeats the inner function 3 times
@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


greet("chabbu")


# class decorators instead of function decorators
# typical used if you want to maintain state
class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    # implement the call method for the decorator
    # allows to execute an object of the class
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"!!! executed {self.num_calls} times")
        return self.func(*args, **kwargs)


# tracks how many times we have executed this function
@CountCalls
def sayHello():
    print("Hello")


sayHello()
sayHello()


# can do timer decorator, debug decorator, check decorator of the args
# can register functions/plugins with decorators
# can cache return values and/or update state
