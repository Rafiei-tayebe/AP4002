import time
from random import Random
from threading import Barrier, Thread

# change our Matrix multiplayer program to run in a multi threaded fashion.
matrix_size = 200
matrix_a = [[0] * matrix_size for a in range(matrix_size)]
matrix_b = [[0] * matrix_size for b in range(matrix_size)]
result = [[0] * matrix_size for r in range(matrix_size)]
random = Random()
# this will signal that all the child threads can start working in the different rows together.
work_start = Barrier(matrix_size + 1)

# This will represent when each thread finishes their work
work_complete = Barrier(matrix_size + 1)


def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row][col] = random.randint(-5, 5)


# each thread compute one row each in the result.
# this function accepts the row number and we can call this function from a separate thread
def work_out_row(row):
    # because we are calling this from a thread and we want to compute multiple matrices,
    # we need to put this into an infinite loop.
    while True:
        # And the way the thread is signaled that there is a row to be computed is with the barrier
        # only when this barrier is unblocked that the work can start
        # and we start computing that row
        work_start.wait()
        for col in range(matrix_size):
            for i in range(matrix_size):
                result[row][col] += matrix_a[row][i] * matrix_b[i][col]
        # And then once we finish, we need to go and wait on the work_complete barrier
        work_complete.wait()

        # We just now need to call it from the different threads that we have.


if __name__ == '__main__':
    # we just need to create a thread for each row that we have
    # row is the number of row in the matrix_a
    # each thread will compute the same row in every iteration
    for row in range(matrix_size):
        Thread(target=work_out_row, args=([row])).start()
    start = time.time()
    for t in range(10):
        generate_random_matrix(matrix_a)
        generate_random_matrix(matrix_b)
        result = [[0] * matrix_size for r in range(matrix_size)]
        # we generated matrix_a and matrix_b in the main thread
        # we need to say all the threads that two matrices are ready for multiplication
        # when we say the main thread (the 201th thread) is also in the wait state,
        # the work_start barrier is unblocked
        work_start.wait()
        # When this happens and all of our threads are waiting on the work to start,
        # the barrier will unblock
        # and each of the threads will work out each row.

        # Then once it finishes, it will go on the work complete barrier.
        # And from the main thread, we just need to be waiting for it,
        # just so we know when the work is finished
        work_complete.wait()

        # and then we start all over again, right with generate there in the matrices,
        # clear results and we signal that the work is ready to start
        # and we keep on doing this for ten times and this is it.
    end = time.time()
    print("Done, time taken", end - start)

# It's not a huge improvement over what we have.
# This particular algorithm is an example of a CPU bound process
