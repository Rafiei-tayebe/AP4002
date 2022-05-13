# Single Threaded Application

import time


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')


if __name__ == '__main__':
    # returns the float value of time in seconds.
    start = time.perf_counter()
    do_something()
    do_something()
    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
