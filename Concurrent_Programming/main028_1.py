# barrier is a simple tool that allows us to synchronize different threads or processes together
# Think about them as being that starting line before the race where every thread comes to that starting
# line and then once they're all in position, release them together.

import time
from threading import Barrier, Thread

# arg: the number of threads that will be participating
barrier = Barrier(2)


# a function that will be called by each one of these threads.
def wait_on_barrier(name, time_to_sleep):
    for i in range(5):
        print(name, "running", round(time.time()-start, 2))
        time.sleep(time_to_sleep)  # the time to sleep before we call this barrier.
        print(name, "is waiting on barrier", round(time.time()-start, 2))
        barrier.wait()
    print(name, "is finished", round(time.time()-start, 2))


start = time.time()
red = Thread(target=wait_on_barrier, args=["red", 4])
blue = Thread(target=wait_on_barrier, args=["blue", 10])
red.start()
blue.start()

# Another operation that is available in Python on these barriers is a way to abort this waiting.
# Once we have aborted a barrier, nothing else can use it.
# time.sleep(8)
# print("Aborting barrier")
# barrier.abort()
# barrier.reset()



