# multi-threaded letter count
# Thread Synchronization solved the race condition issue accrued in main019
import threading

import requests
import time


# pass new parameter to our function: mutex
def count_letters(url, frequency, mutex):
    txt = requests.get(url).text  # the slowest part of our function
    #mutex.acquire()  # It is an important decision: where to acquire/release the lock?
    for letter in txt:
        mutex.acquire()
        letter = letter.lower()

        if letter in frequency:
            frequency[letter] += 1
    mutex.release()
    # the only part we did not protect is the downloading part (which is an IO bound task)
    # the sequential part is quite fast.


def main():
    mutex = threading.Lock()
    frequency = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = time.perf_counter()

    threads = []
    for i in range(1000, 1020):
        url = f"https://www.rfc-editor.org/rfc/rfc{i}.txt"
        t = threading.Thread(target=count_letters, args=(url, frequency, mutex))
        t.start()
        threads.append(t)

    # join is also another synchronization method
    # the parent tread will lock until the child thread is terminated.
    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(frequency)
    # print(json.dumps(frequency, indent=4))
    print(f"Done, time taken: {round(finish - start, 2)} second(s)")


if __name__ == '__main__':
    main()
