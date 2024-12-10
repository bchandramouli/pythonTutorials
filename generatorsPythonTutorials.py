#!/usr/bin/env python3
import sys
from sys import getsizeof


#thanks to @patloeber's youtube channel

# can iterator and generate items lazily
# return only when asked - so are very memory efficient and useful

# defined like normal function but with a yield instead of return

# see till the end for the cool applications

# can have multiple yields
def myGenerator():
    yield 3
    yield 2
    yield 1

g = myGenerator()
print(g)

value = next(g) # keep going till the next yield with state remembered
print(value)

value = next(g) # keep going till the next yield with state remembered
print(value)

value = next(g)
print(value)

# WILL ONLY PRINT 3 ! as we are remembering state!
for i in g:
    print(i)


#reset g
g = myGenerator()
# can be used as inputs to functions that take iterables
print(sum(g))


g = myGenerator()
# generate a list
print(sorted(g))


def countdown(num):
    print('starting')
    while num > 0:
        yield num
        num -= 1

# lazy assignment - does not run anything
cd = countdown(4)

def sum(x):
    try:
        return (next(x) + sum(x))
    except StopIteration:
        return 0

print(sum(cd))

# return numbers from 0 to n
def firstN(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

# replace above with a generator
def first_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1

# with lists
myList = firstN(10)
print(myList)

# with generators
print(list(first_gen(10)))

print(f"size of list function is {sys.getsizeof(firstN(1000000))}")
# whack a mole - look at the size used by the generator - woohoo!
print(f"size with generator is {sys.getsizeof(first_gen(1000000))}")

# this is interesting in python...
a, b = 0, 1
a, b = b, a+b
print(f"a is {a}")
print(f"b is {b}")

def fib(limit):
    n1, n2 = 0, 1
    while (n1 < limit):
        yield n1
        n1, n2 = n2, n1+n2 # whack a mole - this auto does old values?

print(list(fib(5)))

# shortcuts for generator expressions!!! similar to list comprehensions
myGenerator = (i for i in range(100000) if i %2 == 0)
print(sys.getsizeof(myGenerator))

# example with list comprehension but look at memeory... :(
myList = [i for i in range(100000) if i % 2 == 0]
print(sys.getsizeof(myList))

