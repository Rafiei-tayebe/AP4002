# use multiprocessing
import multiprocessing
import time


def do_something():
    print(f'Starting work...')
    i = 0
    for _ in range(20000000):
        i += 1
    print(f'Finished work...\n')


if __name__ == '__main__':
    start = time.perf_counter()
    # The processes list is used to keep track of all newly created processes
    processes = []
    for _ in range(8):
        p = multiprocessing.Process(target=do_something, args=())
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')

# Check: Windows Performance Monitor
