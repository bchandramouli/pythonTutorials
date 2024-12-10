#!/usr/bin/env python3 

#thanks to @patloeber's youtube channel


#set - unordered, mutable, but only unqiue values (no duplicates)
# uses {} to define

mySet = {1, 2, 3}
myset = {} # this is not a set but an empty dict
print(type(mySet))
myset = set() # creates an empty set

# Great way to count distinct chars in a string
mySet = set("Hello")
print(mySet) # see output as {'e', 'o', 'H', 'l'} :) as the set is onordered

#append values
mySet.add('f')
mySet.add(4) # can add integer to the set
print(mySet)

#set is iterable 
for i in mySet:
	print(i)

#check presence in set
if 4 in mySet:
	print('yes')
else:
	print('no')


#unions
odds = {1, 3, 5, 7}
evens = {2, 4, 6, 8}

u = odds.union(evens)
print(u)

#intersetions
i = odds.intersection(evens)
print(i) # empty set


d = odds.difference(evens)
print(d) # returns all elements in first but not in second

d.add(8)
print(u.symmetric_difference(d)) #prints numbers different in both set not just first one


print(u.update(evens)) #adds things to u

print(d.issubset(u)) #check for subsets
print(d.issuperset(u)) #check for superset


f = u #reference assignment not a copy
f.add(20)
print(u)

# proper copy type 1
f = u.copy()
print(f)

# proper copy 2
f = set(u)
print(f)

#frozen set cannot be updated but union intersection and difference can be done
g = frozenset(u)


