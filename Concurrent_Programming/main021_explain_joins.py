import time
from threading import Thread


def child():
    print('Child Tread is doing work...')
    time.sleep(1)
    print('Child Thread done!')


def parent():
    t = Thread(target=child, args=())
    t.start()
    print('Parent Thread in waiting child thread to finish')
    t.join()  # we can also provide a timeout argument
    print('Parent Thread in unlocked')


# call the parent function in our main Thread
parent()
