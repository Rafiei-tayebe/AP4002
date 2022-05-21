# Condition Variables
# issue: sometimes money in the bank would become negative which is invalid
# solution: use condition variable instead of mutex (Lock)
# when the money is not enough we should fo a conditional wait
# when we are calling this wait operation, on condition variable the lock is released.
# lock must be released, otherwise stingy is not allowed to increase money.
# This is the very important property of Condition variable
# mutex (Lock variable) does not have this feature so we use another variable : Condition
# 1. spendy acquires lock
# 2. checks the condition, if condition is True, waits for a signal and releases the lock
# 3. stingy acquires the lock, changes the money, notifies (sends signal) to other threads
#    that things might be changed and stingy releases the lock
# 4. signal wakes up the other thread, so spendy wakes up, acquires the lock, checks the condition
#    and spends money

import threading
from threading import Thread, Lock


class StingySpendy:
    def __init__(self):
        self.money = 100
        # initialize mutex with Lock
        self.cv = threading.Condition()  # change lock to Condition variable

    def spendy(self):
        for i in range(500000):  # changed
            self.cv.acquire()  # spendy acquires lock
            while self.money < 20:  # spendy checks the condition
                self.cv.wait()  # if the condition is True, spendy waits and releases the lock
                # when stingy thread sends the signal, spendy thread wakes up and
                # checks the condition again.
            self.money -= 20  # if the condition is False, spendy thread decreases the money
            if self.money < 0:
                print("Money in the bank:", self.money)
            self.cv.release()  # and finally releases the lock
        print("Spendy Done")

    def stingy(self):
        for i in range(1000000):
            self.cv.acquire()  # stingy thread acquires the lock
            self.money += 10  # stingy thread increases the money
            self.cv.notify()  # stingy thread sends the signal to any waiting thread
            # that the condition might not be valid anymore
            self.cv.release()  # stingy thread releases the lock
        print("Stingy Done")


ss = StingySpendy()
t1 = Thread(target=ss.stingy, args=())
t2 = Thread(target=ss.spendy, args=())

t1.start()
t2.start()

t1.join()
t2.join()

print("Money in the end", ss.money)  # Money in the end 100
