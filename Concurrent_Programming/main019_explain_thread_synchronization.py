# Issue: Race Condition
# Solution: Thread Synchronization using mutex Lock
from threading import Thread, Lock


class StingySpendy:
    def __init__(self):
        self.money = 100
        # initialize mutex with Lock
        self.mutex = Lock()

    def stingy(self):
        for i in range(1000000):
            # before updating money try to acquire the lock (mutex)
            # this function blocks other threads' access to this mutex
            self.mutex.acquire()
            # update money (the shared variable)
            # we can not update this variable without holding that mutex
            self.money += 10
            # after we update the balance we must release the mutex
            # otherwise, others can not access to the mutex and can not update money
            self.mutex.release()
        print("Stingy Done")

    def spendy(self):
        for i in range(1000000):
            self.mutex.acquire()
            self.money -= 10
            self.mutex.release()
        print("Spendy Done")


ss = StingySpendy()
t1 = Thread(target=ss.stingy, args=())
t2 = Thread(target=ss.spendy, args=())

t1.start()
t2.start()

t1.join()
t2.join()

print("Money in the end", ss.money)  # Money in the end 100
