#!/usr/bin/env python3

#thanks to @patloeber's youtube channel

# generate pseudo-random numbers
import random

# pick a random float between 0 and 1
a = random.random()
print(a)

# pick an interger between 1 and 9
b = random.randrange(1, 10)
print(b)

# picks from a normal distribution of mean 0 and std of 1
c = random.normalvariate(0, 1)
print (c)

# pick a random element from the list
mylist = list("ABCDEFGHIJKLMNOP")
a = random.choice(mylist)
print(a)
# picks multiple unique elements from a list
b = random.sample(mylist, 3)
print(b)
# picks same element more than once
c = random.choices(mylist, k=3)
print(c)
# shuffles a list in place
random.shuffle(mylist)
print(mylist)


# give it a seed as these are pseudo-random numbers
random.seed(1)
print(random.random())
print(random.randint(1, 10))

# reseed with the different seed
random.seed(2)
print(random.random())
print(random.randint(1, 10))

# reseed with the same seed 1
random.seed(1)
print(random.random())
print(random.randint(1, 10))

# reseed with the same seed 2 to produce same results
random.seed(2)
print(random.random())
print(random.randint(1, 10))

# for crypto and security use secrets
# for passwords, security tokens and account authentications
# takes longer but generate true random numbers
import secrets

# random integer 10 not included
a = secrets.randbelow(10)
print(a)

# returns an integer with k random bits
b = secrets.randbits(4)
print(b)

# picks a random choice that is not reproducible
c = secrets.choice(mylist)
print(c)

# can also use numpy
# it uses a different random number generator than standard python
import numpy as np

# produces a 1-d array with 3 random floatsd
a = np.random.rand(3)
print(a)

# produce a 3x3 array
b = np.random.rand(3, 3)
print(b)

# random integers 1-d array
c = np.random.randint(0, 10, 1)
print(c)

# random integers multi-d array
d = np.random.randint(0, 10, (3,4))
print(d)

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
# use the rng instead of just shuffle for multi-d arrays!
rng = np.random.default_rng()
rng.shuffle(arr)
print(arr)

# can also set the seed in numpy
np.random.seed(1)
print(np.random.rand(3,3))
# to reproduce the same results
np.random.seed(1)
print(np.random.rand(3,3))