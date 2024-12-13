#!/usr/bin/env python3
# thanks to @patloeber's youtube channel

# Let's start with multiprocessing

import os
from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue  # import Queue from multiprocessing, not queue!
import time

from multiprocessing import Pool

# Processes will need shared memory data to share info
# either a shared value or a shared array


def inc100(n, nums, lockInc):
    for i in range(100):
        # need a lock and use the lock context manager instead of acquire and release
        with lockInc:
            n.value += 1
            for i in range(len(nums)):
                nums[i] += 1
        time.sleep(0.1)


def square(nums, q):
    for i in nums:
        q.put(i * i)


def negate(nums, q):
    for i in nums:
        q.put(-i)


def cuber(num):
    return num * num * num


# use this to ensure that the code responsible for creating new processes
# is only executed when the script is run directly, not when it's imported
# as a module.
if __name__ == "__main__":
    # create a list to store process
    processes = []
    num_processes = os.cpu_count()
    print(f"num cores = {num_processes}")

    shared_number = Value("i", 0)
    print("Number at beginning is", shared_number.value)

    shared_array = Array("d", [0.0, 100.0, 200.0])
    print("Array at the beginning is", shared_array[:])

    lock = Lock()

    # create a process
    for i in range(num_processes):
        # target is the entry point
        # args tuple needs a comma at the end
        p = Process(target=inc100, args=(shared_number, shared_array, lock))
        processes.append(p)

    # start the processes
    for p in processes:
        p.start()

    # join the processes and wait for all of them to complete
    # block the main thread till all of the sub processes finish
    for p in processes:
        p.join()

    print("number at end of main is ", shared_number.value)
    print("Array at the beginning is", shared_array[:])

    # Using queuees
    q = Queue()
    numbers = range(1, 10)

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=negate, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # dont have to join the q as there is no such method, but we can do this
    while not q.empty():
        print(q.get())

    # Process pool can be used to manage multiple worker process
    # can split data into smaller chunks for parallel processing

    pool = Pool()
    # most important methods are map, apply, join, and close

    numbers = range(10)

    # That's it - does mapping, distributes to different processes and returns a result!
    result = pool.map(cuber, numbers)
    # If only one argument needed - pool.apply(cuber, numbers[0])

    pool.close()
    pool.join()

    print(result)  # prints an array of numbers cubed!!!


# Asynchronous calls to map and apply for a different day!!!
