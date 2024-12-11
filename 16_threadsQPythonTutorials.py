#!/usr/bin/env python3
#thanks to @patloeber's youtube channel
import os
# let's do threading now
from threading import Thread, Lock, currentThread
from queue import Queue
import time

def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            # as q's are thread safe, only print needs to be protected
            print(f'in {currentThread().name} got {value}')
        q.task_done()

# use this to ensure that the code responsible for creating new processes
# is only executed when the script is run directly, not when it's imported
# as a module.
if __name__ == "__main__":

    q = Queue()
    lock = Lock()
    num_threads = 20

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        # default is not a daemon thread
        # daemon threads are background thread that get killed when the main thread is done
        thread.daemon= True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    # q.get and q.put calls are all thread safe

    # blocks until all items in the q are processed!
    q.join()

    # join the threads
    # for t in threads:
    #    t.join()
    # no need for the joins...
    # IMP: when the main thread is done, all the daemon threads are also killed!
