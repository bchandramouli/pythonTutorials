#!/usr/bin/env python3
#thanks to @patloeber's youtube channel

import copy

old = 5
new = old # creates a new reference to 5 no problem for immutable types
new = 6 # refers to a immutable 6
print (old)
print(new)

# lists though are mutable
# shallow copuy is only one level deep - only copies nested references of the child
# deep copy - full independent copy
my_list = [1, 2, 3, 4]
cpy_list = copy.copy(my_list)
cpy_list[0] = -10
print(my_list)
print(cpy_list)

# many ways to copy lists - shallow copies only - as the children are immutable
cpy_list = my_list.copy()
cpy_list = list(my_list)
cpy_list = my_list[:] # slicing operator

# npow if we have nested lists
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
print(nested_list)
# shallow copy
cpy_list = copy.copy(nested_list)
cpy_list[0] = [10, 20, 30] # will not change the original
cpy_list[0][1] = -10 # ouch will impact original as it is second level
print(cpy_list)
print(nested_list)  # ouch original changed in the second level

nested_list = [[1,2,3], [4,5,6], [7,8,9]]
cpy_list = copy.deepcopy(nested_list)
cpy_list[0][1] = -10 # aha original not impacts
print(cpy_list)
print(nested_list)  # ouch original changed in the second level


# can use copying for classes too

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Alex', 23)
p2 = p1

p2.age = 28 # ouch impacts both orig and new
print(p2.age)
print(p1.age)

p1 = Person('Alex', 23)
p2 = copy.copy(p1)
p2.age = 28 # orig not impacted
print(p2.age)
print(p1.age)

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person('Alex', 55)
p2 = Person('Joe', 25)
c = Company(p1, p2)
newC = copy.copy(c) # shallow copy
# newC = copy.deepcopy(c) - pls use deep copy to make it work!
newC.boss.age = 56
print(newC.boss.age)
print(p1.age) # ouch changed




