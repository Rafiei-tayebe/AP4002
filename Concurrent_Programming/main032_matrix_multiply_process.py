# This program runs with processors instead of threads.
# change imports
import multiprocessing
import time
from random import Random

from multiprocessing import Barrier

from multiprocessing.context import Process

process_count = 7  # I have 8 cores
matrix_size = 200
random = Random()


# We need to change the access so it doesn't use a two dimensional array.
def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row * matrix_size + col] = random.randint(-5, 5)


# each process will be computing multiple rows, we will pass the id of process
# the process number 0 will compute row 0, 8, 16, ...
# we are not sharing memory between processes, so we need to pass them in the input
def work_out_row(id, matrix_a, matrix_b, result, work_start, work_complete):
    while True:
        work_start.wait()
        for row in range(id, matrix_size, process_count): # (0, 200, 8)
            for col in range(matrix_size):
                for i in range(matrix_size):
                    # math trick to change 2d matrix to 1d matrix
                    # because the shared memory area only allows us to pass one dimensional
                    result[row * matrix_size + col] += matrix_a[row * matrix_size + i] * matrix_b[i * matrix_size + col]
        work_complete.wait()


if __name__ == '__main__':
    # the start method of each process
    # multiprocessing.set_start_method('spawn')
    work_start = Barrier(process_count + 1)  # number of processes that we have
    work_complete = Barrier(process_count + 1)
    # instead of waiting for matrix size plus one, we need to wait for process count plus one.

    # initialize our input matrices and the result one.
    # no override, no need to lock
    matrix_a = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    matrix_b = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    result = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)

    for p in range(process_count):
        Process(target=work_out_row, args=(p, matrix_a, matrix_b, result, work_start, work_complete)).start()

    start = time.time()
    for t in range(10):
        generate_random_matrix(matrix_a)
        generate_random_matrix(matrix_b)
        for i in range(matrix_size * matrix_size):
            result[i] = 0
        # We signal that there is work by work_start.wait()
        # it will unblock all the processes and then we wait for the work to be completed on the second barrier.
        work_start.wait()
        work_complete.wait()
    end = time.time()
    print("Done, time taken", end - start)
