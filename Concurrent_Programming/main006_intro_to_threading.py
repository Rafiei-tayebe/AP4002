"""
# Using Python threading to develop a multi-threaded program example
To create a multi-threaded program, you need to use the Python threading module.

1. Import the Thread class from the threading module.
2. Create a new thread by instantiating an instance of the Thread class.
    The Thread() accepts many parameters. The main ones are:
        + target: specifies a function (fn) to run in the new thread.
        + args: specifies the arguments of the function (fn). The args argument is a tuple.
3. Start the thread by calling the start() method of the Thread instance
4. If you want to wait for the thread to complete in the main thread, you can call the join() method.
    + By calling the join() method, the main thread will wait for the second thread to complete before it is terminated

When the program bellow executes, it’ll have three threads:
    + the main thread is created by the Python interpreter,
    + and two new threads are created by the program.
"""
# 1. Import threading module.
import threading
import time


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')


if __name__ == '__main__':
    # returns the float value of time in seconds.
    start = time.perf_counter()

    # 2. Create new thread(s) by instantiating an instance of the Thread class.
    # target: specifies a function (fn) to run in the new thread.
    t1 = threading.Thread(target=do_something)
    t2 = threading.Thread(target=do_something)

    # 3. start the thread by calling the start() method of the Thread instance
    t1.start()
    t2.start()

    # 4. If you want to wait for the thread to complete in the main thread, you can call the join() method.
    # This blocks the calling thread until the thread whose join() method is called terminates
    t1.join()
    t2.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
