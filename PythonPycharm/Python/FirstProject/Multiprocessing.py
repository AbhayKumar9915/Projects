"""
Multiprocessing creates separate processes, each with its own memory space
multiple CPU cores, bypasses GIL limitations in CPython,
child processes are killable(ex. function calls in program) and is much easier to use
Multiprocessing
1.Process
2.Separate memory
3.Higher memory uses
4.Bypasses GIL
5.Uses multiprocessing module
"""

import multiprocessing
import time


def calculate_square(n):
    print("Calculating square of {}".format(n))
    time.sleep(1)
    return n*n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    # With one process
    start_one_p = time.time()
    with multiprocessing.Pool(processes=1) as pool:
        results = pool.map(calculate_square, numbers)
        end_one_p = time.time()
        print("Squares {}".format(results))

    # With 5 processes
    start_five_p = time.time()
    with multiprocessing.Pool(processes=5) as pool:
        results = pool.map(calculate_square, numbers)
        end_five_p = time.time()
        print("Squares {}".format(results))

        print("Time taken in running with 1 process: ", end_one_p - start_one_p)
        print("Time taken in running with 5 process: ", end_five_p - start_five_p)
