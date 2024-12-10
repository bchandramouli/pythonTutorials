#!/usr/bin/env python3 

#thanks to @patloeber's youtube channel

#itertools: product, permutations, combinations, accumulate, groupby, and infinite

from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a,b) # computes the cartesian product of a and b
print(list(prod))

b = [3]
prod = product(a,b,repeat=2) #can also add optional arg of repeating it
print(list(prod))


from itertools import permutations
# returns all ordering of inputs
a = [1, 2, 3]
perm = permutations(a)
print(perm)
print(list(perm))

perm = permutations(a, 2) # setup optional length of 2 in the result permutations
print(list(perm))


# no replacements (1,2), (1,3), (1,4) no (1,1)
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2) #needs the argument of n and r
print(list(comb)) 

# make combinations with itself included e,g (1,1)
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr)) 


from itertools import accumulate
a = [1, 2, 3, 5, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc)) # default successive sums computed

import operator
acc = accumulate(a, func=operator.mul)
print(list(acc))

acc = accumulate(a, func=max)
print(list(acc))


# returns keys from an interable
from itertools import groupby

def lesserThan3(x):
	return(x < 3)
a = [1, 2, 3, 4]
groupObj = groupby(a, key=lesserThan3) # gives us an iterable! wowzersss
print(groupObj)
for key, value in groupObj:
	print(key, list(value)) # prints True [1, 2], False [3, 4] WOWOOWOWOWO

# another example to concretize
# now groupby will only groupby contiguous elements, so sort before using groupby
persons = [{'name': 'tim', 'age': 25}, {'name': 'lisa', 'age': 25},
			{'name': 'datu', 'age': 27}, {'name': 'claire', 'age': 25}]
groupObj = groupby(persons, key=lambda x: x['age']) # gives us an iterable! wowzersss
for key, value in groupObj:
	print(key, list(value)) # prints True [1, 2], False [3, 4] WOWOOWOWOWO


#infinites - count, cycle, repeat
from itertools import count, cycle, repeat

# an infinite loop starting at 10
for i in count(10):
	print(i)
	if i == 17:
		break


# cycle infinitely through an iterable
a = [1, 2, 3]
for i in cycle(a):
	print(i)
	if i == 3: # need a condition to stop else will keep going
		break

# infinite loop with just the first arg. Secong arg tells how many times to repeat
for i in repeat(1, 4):
	print(i)