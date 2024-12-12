"""
- positional and keyword arguments
- default arguments
- variable-length arguments (*args, and **kwargs)
- Container unpacking into function arguments
- local and gloabal args
- parameter passing by value or by reference
"""

def print_name(name):
    print(f"Name is {name}")

def foo(a, b, c, d=4):
    print(a, b, c, d)

# one * - any number of positional arguments - *args
# two ** - any number of keyword arguments - **kwargs
def fargs(a, b, *args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    # kwargs is a tuple
    for key in kwargs:
        print(f"{key} : {kwargs[key]}")

def stargs(a, b, *, c, d):
    print(a,b, c, d)

print_name('China')
# d is the default argument, default args must be at the end
# we can use keywords arguments => order of the arguments will not matter
foo(a=100,c=300, b=200)
# can mix positional and keywords args, but positional have to be first!
foo(100, 200, c=200)

fargs(1, 2)
fargs(1, 2)
fargs(1, 2, c = 100)
fargs(1, 2, 3, 4, 5, c=8, d=9, e = 10)
# forcing keyword arguments to be present!
# after the star the keyword arg has to be provided mandatorily
stargs(1, 2, c=3, d=4)

#unpacking a list as arg list to a function
my_list = [10, 20, 30]
# needs *
foo(*my_list)

# length and the keys must match the parameter names!
my_dict = {'a': 100, 'b':200, 'c': 300}
# needs **
foo(**my_dict)