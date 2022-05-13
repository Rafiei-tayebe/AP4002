# Explain: Race Condition
from threading import Thread


class StingySpendy:
    def __init__(self):
        self.money = 100

    def stingy(self):
        for i in range(1000000):
            self.money += 10
        print("Stingy Done")

    def spendy(self):
        for i in range(1000000):
            self.money -= 10
        print("Spendy Done")


ss = StingySpendy()
t1 = Thread(target=ss.stingy, args=())
t2 = Thread(target=ss.spendy, args=())

t1.start()
t2.start()

t1.join()
t2.join()

print("Money in the end", ss.money)  # Money in the end 1911640 ?
