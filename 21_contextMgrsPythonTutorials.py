#!/usr/bin/env python3
#thanks to @patloeber's youtube channel

"""
- tools for resource management
- example with open, lock, etc...
"""

from contextlib import contextmanager

# the with will handle everything like closing files even in the case of exceptions
# does what resource freeing, one would have to do with finally
with open('info.txt', 'w') as file:
    file.write('alpha beta gamma and delta rays')

# open and close db connections

# for locks - see tutorial 15 and 16

# context managers for classes
# implement the enter and exit methods
class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    # executed on entering the with statement
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            print('closing the file`')
            self.file.close()
        print('exc: ', exc_type, exc_value, exc_traceback)
        if exc_type is not None:
            print('exception handled')
        print('exit')
        return True

with ManagedFile('info.txt') as file:
    print('write to file')
    file.write('abcradabra')
    file.some()
print('out of with')


# we can use context managers with functions too

# need to decorate it with the context manager
@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f # temporarily gives up context of this function
        # also helps us to handle exceptions here instead of in the with
    finally:
        # free up the resource when the execution of this function comes back
        f.close()


with open_managed_file('info.txt') as f:
    f.write('anda gunda go')