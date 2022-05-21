import threading
import os
from os.path import join, isdir
import time

# this variable will contain list of paths containing our file.
# we use multiple threads to update this variable
matches = []
# we should acquire this mutex when updating matches list
mutex = threading.Lock()


# every time we call file_search function, we should make a thread
# no mather it is a recursive call or it is an ordinary call
# we need to append all threads inside the function to a list and join them in a separate loop
def file_search(root: str, filename: str) -> None:
    """
    :param root: The path to search in
    :param filename: the filename to search for
    :return: None
    """
    print('Searching in:', root)
    child_threads = []
    for file in os.listdir(root):
        full_path = join(root, file)  # concatenates root with file
        if filename in file:
            mutex.acquire()  # mutex
            matches.append(full_path)
            mutex.release()  # mutex
        if isdir(full_path):
            t = threading.Thread(target=file_search, args=(full_path, filename))
            t.start()
            child_threads.append(t)
    for thread in child_threads:
        thread.join()


def main():
    b = time.time()
    path = 'C:/Users/Tayebe Rafiei/Desktop'
    t = threading.Thread(target=file_search, args=(path, 'main'))
    t.start()
    t.join()
    for m in matches:
        print('Matched:', m)
    print(f"Done, time taken: {round(time.time() - b, 2)} second(s)")


if __name__ == '__main__':
    main()
