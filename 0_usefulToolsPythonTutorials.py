#!/usr/bin/env python3 

#thanks to @patloeber's youtube channel

import timeit

# if GC measurements are needed? timeit turns off GC while timing :)
#timeit.Timer('for i in range(10): oct(i)', 'gc.enable()').timeit()


print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000)) #lists take much longer to create
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000)) #being immutable malloc only once
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))
print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))


from timeit import default_timer as timer

my_list = ['a'] * 100000

start = timer()
mystring = ''
for i in my_list:
	mystring += i
end = timer()
print('manual join time = ', end-start)

start = timer()
myString = ''.join(my_list)
end = timer()
print('manual join time = ', end-start)
