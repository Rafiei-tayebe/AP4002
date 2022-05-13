# multi-threaded letter count
# Race Condition
import json
import threading

import requests
import time


def count_letters(url, frequency):
    txt = requests.get(url).text
    for letter in txt:
        letter = letter.lower()
        if letter in frequency:
            frequency[letter] += 1


def main():
    frequency = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = time.perf_counter()

    threads = []
    for i in range(1000, 1020):
        url = f"https://www.rfc-editor.org/rfc/rfc{i}.txt"
        t = threading.Thread(target=count_letters, args=(url, frequency))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    # print(frequency)
    print(json.dumps(frequency, indent=4))
    print(f"Done, time taken: {round(finish - start, 2)} second(s)")


if __name__ == '__main__':
    main()
