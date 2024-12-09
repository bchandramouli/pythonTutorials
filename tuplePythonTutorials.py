#!/usr/bin/env python3

# tuple is ordered and immutable - cannot be changed after creation

myStringlikeTuple = ("Max") # this is a string and not a tuple
print(type(myStringlikeTuple))

mytestTuple = ("Max",) #this is a tuple and not a string
 
myTuple = ("Moin", "560 hemming way", "Santa Cruz", 94040)

print(myTuple[0]) # can cause index overflow/underflow
print(myTuple[-1]) # -1 is the last item

# iterate a tuple
for i in myTuple:
	print(i)

# check presence in the tuple
if "Moin" in myTuple:
	print("yes")
else:
	print("no")

print(len(myTuple))

# check presence and print location
print(myTuple.count('Moin'), myTuple.index('Santa Cruz'))

#splicing
newTuple = myTuple[1:200] #it auto picks last index
print(newTuple)

#can also do an optional step argument ::2 like in lists. 

#mappping elements to tuple indices
name, street, *city = myTuple 

# as we have the zip cannot unpack to 3 values. Add a * to city to make it a list
zipcode = city[1]

print(name, street, city[0], zipcode)


