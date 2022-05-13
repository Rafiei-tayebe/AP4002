"""
# Using Python multiprocessing to develop a multi-processed program example
To create a multi-processed program, you need to use the Python multiprocessing module.

1. Import the Process class from the multiprocessing module.
2. Create a new process by instantiating an instance of the Process class.
    The Process() accepts many parameters. The main ones are:
        + target: specifies a function (fn) to run in the new process.
        + args: specifies the arguments of the function (fn). The args argument is a tuple.
3. Start the process by calling the start() method of the Process instance
4. If you want to wait for the process to complete in the main process, you can call the join() method.
    + By calling the join() method, the main process will wait for the second process to complete before it is terminated

When the program bellow executes, it’ll have three processes:
    + the main process is created by the Python interpreter,
    + and two new processes are created by the program.
"""
# 1. Import multiprocessing module.
import multiprocessing
import time

# returns the float value of time in seconds.
start = time.perf_counter()


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')


if __name__ == '__main__':
    # 2. Create new process(es) by instantiating an instance of the Process class.
    # target: specifies a function (fn) to run in the new process.
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    # 3. start the process by calling the start() method of the Process instance
    p1.start()
    p2.start()

    # 4. If you want to wait for the process to complete in the main process, you can call the join() method.
    p1.join()
    p2.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
