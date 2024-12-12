#!/usr/bin/env python3
# thanks to @patloeber's youtube channel

"""
- * -  the cool operations
- multiplication and power operations
- creation of lists, tuples with repeat elements
- *args, **kwargs
- for unpacking lists, tuples, or dictionaries into func args
- for unpacking containers into lists
- for merging containers, and dictionaries
"""

# multiplication
result = 5 * 7
print(result)

# power
pow = 5**2
print(pow)

# create lists with repeat elements
my_list = [0, 1] * 10
print(my_list)  # list of 5 zeros and 5 1s alternating
abStr = "AB" * 10
print(abStr)  # 20 cha string with repeating ABAB...


# positional *args and keyword **kwargs - see lesson 18 for more!
def fargs(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    # kwargs is a tuple
    for key in kwargs:
        print(f"{key} : {kwargs[key]}")


fargs(1, 2, 3, 4, c=5, d=6)

# unpacking lists and dicts into functional args - again see lesson 18
my_list = [0, 1, 2]
fargs(*my_list)

# unpack lists into variables
numbers = [1, 2, 3, 4, 5, 6]
*begin, last = numbers
print(f"begin is {begin}")  # begin is a list
print(f"last is {last}")
begin, *last = numbers
print(f"begin is {begin}")
print(f"last is {last}")  # last is a list
begin, *middle, last = numbers
print(f"begin is {begin}")
print(f"middle is {middle}")  # middle is a list
print(f"last is {last}")

# merge tuples/lists/sets into a list
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

# unpack and merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict_new = {**dict1, **dict2}
print(dict_new)
