# Passing arguments to threads
# 9.18 secs
import threading
import time


def do_something():
    print(f'Starting work...')
    i = 0
    for _ in range(20000000): 
        i += 1
    print(f'Finished work...\n')


if __name__ == '__main__':
    start = time.perf_counter()
    # The threads list is used to keep track of all newly created threads
    threads = []
    for _ in range(10):
        t = threading.Thread(target=do_something, args=())
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
