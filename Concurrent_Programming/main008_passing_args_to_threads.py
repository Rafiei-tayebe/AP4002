# Passing arguments to threads
import threading
import time


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print(f'Done sleeping...')


if __name__ == '__main__':
    # returns the float value of time in seconds.
    start = time.perf_counter()
    # The threads list is used to keep track of all newly created threads
    threads = []
    for _ in range(10):
        # The Thread() accepts many parameters. The main ones are:
        #         + target: specifies a function (fn) to run in the new thread.
        #         + args: specifies the arguments of the function (fn). args is a tuple.
        t = threading.Thread(target=do_something, args=[1])
        t.start()

        threads.append(t)

    # wait for all threads to complete by calling the join() method
    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
