#!/usr/bin/env python3
# thanks to @patloeber's youtube channel


# tip 1: merge append list declarations
# use init instead of appending one by one

# tip 2: iterate over dict.items() instead of accessing 1 by 1

# tip3: replace range(len..) with enumerate
# for i in range(len(foo)):
# enumerate is more useful pls, and includes a start counter too
# for i, num in enumerate(nums, start= 1)

numbers = [1, 2, 3, 4]
# ready unpacking, optional start will given different index numbering if needed
for idx, val in enumerate(numbers, start=1):
    print(idx, val)

# instead of
for i in range(len(numbers)):
    print(i, numbers[i])

# tip 4: replace manual counters with enumerate
# i+= 1 with len(nums)

# tip 5: simplify condition True/False directly into return call
# e.g return bool(list) instead of return (True/False) etc.

# tip 6: merge duplicates into conditionals
# use or and and

# tip 7: use multiple comparisons with in operator
# if currency in ["US", "EUR"] instead of currency == "US" and currency == "EUR"
# even better use a set!

# tip 8: replace yield in for loop with yield from for iterables
# instead of for block in entry.get_blocks():
#       yield block
# do like this yield from entry.get_blocks()!!! Avoids the manual looping


# tip 9: think lazy and use geenrators
events = [("learn, 5"), ("learn", 10), ("relaxed", 20)]
min_studied = 0
for event in events:
    if event[0] == "learn":
        min_studied += event[1]
print(min_studied)

# can be replaced by a generator with list comprehension
study_times = (event[1] for event in events if event[0] == "learn")
min_studied = sum(study_times)
print(min_studied)


# NOW CAUTION!!!
# remember when you use a generator it yields and
# it will run out of values. :)))


# use itertools please when you can!


# python onliners!
# swap variables
a = 5
b = 10
a, b = b, a

# list comprehension
squares = [i * i for i in range(10)]

# if else in one line
var = 20 if 3 > 2 else 29

# print only elements
my_list = [1, 2, 3, 4, 5]
print(*my_list)  # unpacks the elements without spaces in the end!

# reverse a list
a = [1, 2, 3, 2, 1]
b = a[::-1]

print(a == a[::-1])  # will check if a is a palindrome

# String to a number
input = "1 2 3 4 5 6"
my_list = list(map(int, input.split()))
print(my_list)

# Reading file into a list
names = [line.strip() for line in open("info.txt", "r")]
print(names)

# start a http server  in the terminal with index.html files
# pyton -m http_server


# use list slicing to copy lists especially while working on the same list in

# if __name__ == "__main__" add this guard statement
# useful when things are imported and also as standalone

# checking file or directory exists instead of try except block
# method 1: use os,path.isfile, os.path.exists
# method 2: use the pathlib module and Path objects

# USE PATHLIB for all file directory operations!!!

# index of an item in a list
# methode 1 my_list.index("key") - wrap in try except, returns only first match

# wrap system commands
# method 1
import subprocess

subprocess.run(["ls", "-l"])
# method 2
import os

os.system("ls -l")

# subprocess is more powerful and is recommended
# example subprocess.popen

# merge dictionaries
x = {"a": 1, "b": 2}
y = {"b": 8, "c": 9}
# method 1
x.update(y)

# method 2
z = x | y

# method 3
z = {**x, **y}

# @classmethod vs @staticmethod
# can be called on both class and instances - dont need instantiation
# class is passed in by default to class methods
# static methods dont have access to the class variables

# difference __str__ and __repr__
# dunder methods
# best to reimplement them for custom classes
# repr must be unabmiguous
# repr is a fallback for str
# repr for developers, str for customers

# concatenate lists
a = [1, 2]
b = [3, 4]
c = a + b
c = [*a, *b]
