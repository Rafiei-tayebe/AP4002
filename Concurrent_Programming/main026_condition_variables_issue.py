# Condition Variables
# issue: sometimes money in the bank would become negative which is invalid
# +10 -10 -10 : spendy spends money that we don't have!
# solution: if we don't have enough money we must make spendy wait!

from threading import Thread, Lock


class StingySpendy:
    def __init__(self):
        self.money = 100
        # initialize mutex with Lock
        self.mutex = Lock()

    def stingy(self):
        for i in range(1000000):
            self.mutex.acquire()
            self.money += 10
            self.mutex.release()
        print("Stingy Done")

    def spendy(self):
        for i in range(500000):  # changed
            self.mutex.acquire()
            self.money -= 20  # changed
            if self.money < 0:
                print("Money in the bank:", self.money)
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
