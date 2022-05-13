# Passing arguments to threads
# 10.17 secs
import time


def do_something():
    print(f'Starting work...')
    i = 0
    for _ in range(20000000):
        i += 1
    print(f'Finished work...\n')


if __name__ == '__main__':
    # returns the float value of time in seconds.
    start = time.perf_counter()

    for _ in range(10):
        do_something()

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
