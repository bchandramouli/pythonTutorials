#!/usr/bin/env python3

# thanks to @patloeber's youtube channel

x = 5

# use try except block
try:
    assert x > 5
except Exception as e:
    print("assertion happend", e)
finally:
    # both exception and finally could happen :)
    # use it mostly for clean ups
    print("all good to go - cleaning up")

# exception example
if x < 0:
    raise Exception("x should be +ve")


# seperate error handling exception
class ValueError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    pass


def test_num(x):
    if x > 100:
        raise ValueError("value is too high", x)
    if x < 5:
        raise valueError("value is too small", x)


try:
    test_num(200)
except ValueError as e:
    print(e)
