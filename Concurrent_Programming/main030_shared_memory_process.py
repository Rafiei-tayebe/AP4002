# Memory Sharing in processes
# matrix multiplication
# the idea is to find an elegant way to convert them to run with processes.
# processes are a lot more heavyweight than threads

# The other problem that we have deals with how process memory sharing works in Python.
# We can only share variables and single dimensional area and to represent our matrix
# we need somehow to map this two dimensional area into a single dimension area.
# We just grab each row and we put it after each other.
# So we have to use a one dimensional area.



import multiprocessing
from multiprocessing.context import Process
import time


def print_array_contents(array):
    while True:
        print(*array, sep=', ')  # prints the content of the array
        time.sleep(1)  # then sleeps for one second


if __name__ == '__main__':
    # arr = [-1]*10  # [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    arr = multiprocessing.Array('i', [-1]*10, lock=True)
    # first argument: the type of members of the array
    # final argument is to decide whether we want to lock access to this area or not
    # When it is true, it means that every access to this area is synchronize.
    # It's equivalent to acquiring a mutex lock

    p = Process(target=print_array_contents, args=[arr])
    p.start()

    # The idea over here is that we will modify this list of numbers from the main process
    # and we will see if that change is reflected in our child process as well.
    for i in range(10):
        # inside this loop, we are going to sleep for two seconds.
        time.sleep(2)
        for j in range(10):
            arr[j] = i

# result:
# you can see it's minus one for two seconds, then it changes to zero, then it changes to one,
# two, and so on every time we increase J in this loop over here.


