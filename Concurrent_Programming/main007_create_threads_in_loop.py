# create threads in a loop
import threading
import time


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')


if __name__ == '__main__':
    start = time.perf_counter()

    threads = []
    for _ in range(10):
        t = threading.Thread(target=do_something)
        t.start()
        threads.append(t)

    # Notice that if you call the join() method inside the previous loop,
    # the program will wait for the first thread to complete before starting the next one.
    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
