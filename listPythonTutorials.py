#!/usr/bin/env python3

#thanks to @patloeber's youtube channel

myList = [0] * 5
print(myList)

myList.append(-2)
myList.append(-1)
myList.append(5)

newList = sorted(myList)
print(newList)

newList = newList[:3]
print(newList)

newList = myList[::2]
print(newList)

#assignment
newList = myList #assignment is not copying, but merely a pointer assugnment
newList.append(200)
print(myList)

#List copying
newList = myList[:] #slicing technique to copy
print(newList)

newList = list(myList) #new instanitation
print(newList)

newList = myList.copy() # dot copy method
print(newList)

#List comprehension
newList = [i*i for i in myList] # wowzers! [expression iteration] in one line
print(newList)
