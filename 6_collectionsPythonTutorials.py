#!/usr/bin/env python3 

#thanks to @patloeber's youtube channel

#implements special container data types than general built-in ones

#counter, named tuple, ordered dict, default dict and the deque

from collections import Counter
a = "aaaabbbccccccc"
# creates a dictionary of the count of unique elements - iterable!
myCounter = Counter(a) 
print(myCounter)
print(myCounter.most_common()) # returns a list with the tuples
print(myCounter.most_common(1)[0][0]) # to get the actual value - try it


from collections import namedtuple

# namedTuple first arg - class name, second arg - set of fields
Point = namedtuple('Point','x, y')
pt = Point(1, -1)
print(pt) # Point(x=1, y=-1) and we can access pt.x and pt.y


from collections import OrderedDict
#just like regular dictionary but remember the order of insertions
# more useful for older python, > 3.7 regular dict also remembers order
ordDict = OrderedDict()
ordDict['a'] = 1
ordDict['b'] = 2
ordDict['c'] = 3
ordDict['d'] = 4
print(ordDict)


from collections import defaultdict
d = defaultdict(int) #can choose the default type for unknown keys
d['a'] = 1
d['b'] = 2
print(d)
print(d['c']) # prints 0 as the default value

d = defaultdict(list) #can choose the default type for unknown keys
d['a'] = 1
d['b'] = 2
print(d)
print(d['c']) # prints an empty list


# double ended queue - implemented very efficiently
from collections import deque
d = deque()
d.append(1) #add to end
d.append(2) #add to end 
print(d)

d.appendleft(30) # add to front
d.append(40) # add to end
print(d)

d.popleft()
print(d) # removes leftmost

d.clear()
print(d) # removes all elements

d.extendleft([4,5,6]) # add to the left in that order so 6 will be leftmost
print(d)

#rotations
d.rotate(1)
print(d)

d.rotate(2)
print(d)

d.rotate(-1) #rotate one place left
print(d)