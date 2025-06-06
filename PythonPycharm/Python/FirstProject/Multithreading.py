"""
Process of running multiple threads in same process
Multithreading
1.Threads
2.Shared memory
3.Lower Memory uses
4.Affected by GIL - Global interpreter lock
5.Uses threading module

Synchronization in python is essential while working with multithreading to prevent race conditions and to ensure
data integrity, as in below program order of print is changing due to race condition.
Lock, RLock, Event()... can be used, but it slows down performance.
"""

from threading import Thread
import time


# This program reduces the time of execution by running tasks in parallel
class Hello(Thread):
    def run(self):
        for i in range(2):
            print('Hello')
            time.sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(2):
            print('Hi')
            time.sleep(1)


class Bye(Thread):
    def run(self):
        for i in range(2):
            print('Bye')
            time.sleep(1)

start_n = time.time()
hello = Hello()
hi = Hi()
bye = Bye()

print("***Normal Execution***")
# Normal execution
hello.run()
hi.run()
bye.run()
end_n = time.time()
print("***Multithreading Execution***")

start_mt = time.time()
# Will execute in parallel
hello.start()
hi.start()
bye.start()

# Joins threads back to the parent process, which is this program
hello.join()
hi.join()
bye.join()
end_mt = time.time()

print("Time taken in normal execution: ",end_n - start_n)
print("Time taken in multithreading execution: ",end_mt - start_mt)

# This comes in main thread and execute at last due to join implementation
# print('Bye')
