#!/usr/bin/env python3

#thanks to @patloeber's youtube channel

# Process is an instance of a program
# + takes advantages of multiple cpus and cores
# + separate memory space => memory not shared between processes
# + great for cpu bound processing
# + new process is started independent of other process
# + processes are interruptable/terminable
# +  one GIL (global interpreter lock) for each process -> avoids GIL issues
# - heavyweight
# - slower than starting a thread
# - more memory
# - IPC is much more complicated

# Threads: an entity with a program that can be scheduled for execution
# Processes can spawn multiple threads
# + lightweight
# + all threads within a process share the same memory
# + starting a thread is faster than starting a process
# + great for I/O bound tasks
# - Limited by the GIL - allows only one thread at a time
# - no effect for CPU bound tasks
# - not interruptable/terminable
# - careful with race conditions and contentions


# GIL: Global Interpreter Lock
# A lock that allows only one thread at a time to execute in python
# Needed because in cpython (underneath implementation for base python)
# the memory management is not thread-safe
# the reference counting method for tracking objects
# this ref count variable needs to be protected from threads that access the same object.
# if multiple threads access - it can leave dangling objects!

# How to get around GIL
# use multi-processing
# use a different python implementation - chaithon or ironpython. Duh!
# use python as a wrapper for 3rd party libraries - used by numpy and scipy!
# they use python wrappers to call code written in C. Nice!!!!


# Let's start with multiprocessing

import os
from multiprocessing import Process
import time

def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)

# use this to ensure that the code responsible for creating new processes
# is only executed when the script is run directly, not when it's imported
# as a module.
if __name__ == "__main__":
    # create a list to store process
    processes = []
    num_processes = os.cpu_count()
    print(f"num cores = {num_processes}")

    # create a process
    for i in range(num_processes):
        # target is the entry point
        p = Process(target=square_numbers)
        processes.append(p)

    # start the processes
    for p in processes:
        p.start()

    # join the processes and wait for all of them to complete
    # block the main thread till all of the sub processes finish
    for p in processes:
        p.join()

    print('end processes in main')


    #
    # Threading!!!
    #

    # let's do threading now
    from threading import Thread, Lock
    import time

    database_value = 0

    def increase(lock):
        global database_value

        # critical section
        # lock.acquire()
        # Recommended way to use lock as a context manager with the critical section
        with lock:
            local_copy = database_value
            local_copy += 1
            time.sleep(0.1) # causes race that both read the old value :(
            database_value = local_copy
        # don't need the release, as the context manager acquires and releases by itself
        # lock.release()

    print(f'start value is {database_value}')

    threads = []
    num_threads = 2

    lock = Lock()
    # setup the threads
    for i in range(num_threads):
        t = Thread(target=increase, args=(lock,))
        threads.append(t)

    # statr the threads
    for t in threads:
        t.start()

    # join the threads
    for t in threads:
        t.join()

    print(f'end threading in main with value {database_value}')


