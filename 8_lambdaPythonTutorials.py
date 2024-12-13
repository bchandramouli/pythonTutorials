#!/usr/bin/env python3

# thanks to @patloeber's youtube channel

# lambda arguments: expressions

addNum = lambda x, y: x + y
print(addNum(2, 3))


points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# sort the array by the y-coordinate
point2dSorted = sorted(points2D, key=lambda points: points[1])

print(points2D)
print(point2dSorted)

# map function
# map(func, seq) - args are a function and a sequence
a = [1, 2, 3, 4]
# using map function
b = map(lambda x: x * 2, a)
print(list(b))

# using list comprehension - see list tutorial
c = [x * 2 for x in a]
print(c)

# filter(func, sequence)
b = filter(lambda x: (x % 2 == 0), a)
print(list(b))
# using list comprehension
c = [x for x in a if x % 2 == 0]
print(c)


from functools import reduce

# reduce(func, sequence)
# repeatedly applies the func to the elements of the sequence and returns a single value.
b = reduce(lambda x, y: x * y, a)
print(b)
