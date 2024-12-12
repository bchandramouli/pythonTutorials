#!/usr/bin/env python3

# thanks to @patloeber's youtube channel

# dictionay - key value pairs, unordered, mutable collection

myDict = {"Name": "Mouli", "Age": 42, "Address": "Mountain View"}

for key in myDict.keys():
    print(key)

for key, value in myDict.items():
    print(key, value)

# copying dictionarires
newDict = myDict  # WRONG - only pointer assignment - not copied
print(newDict)

newDict["Email"] = "mba@abm.com"
print(myDict)

# correct copying
newDict = dict(myDict)
print(newDict)

# merging dictionaries
newDict = {"Email": "mba@abm.com"}
print(newDict)
myDict.update(newDict)
print(myDict)

# dict to list
myList = myDict.values()
print(myList)


# tuple can be used as a key in a dictionary!
myTuple = (0, 7)
myDict = {myTuple: 15}
print(myDict)
