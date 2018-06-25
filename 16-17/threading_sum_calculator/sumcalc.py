import threading
import time


class SumCalc(threading.Thread):
    """
    Iterates over a range of numbers and adds them to another one using threads

    :ivar int total: Current number
    :ivar lock: The lock

    """

    total = 0   # class global total
    lock = threading.Lock()

    def __init__(self, count_from, count_to):
        """
        Initializes the sum calculators variables

        :param count_to: the number the thread is supposed to count to, starting from 1
        """
        threading.Thread.__init__(self)
        self.count_from = count_from
        self.count_to = count_to

    def run(self):
        """
        Adds the addend to total until the addend reaches the value of num
        """
        for j in range(self.count_from, self.count_to):
            with SumCalc.lock:
                SumCalc.total += j


thread_default_count = 3

num = input("Which value do you want to count to?")
thread_num = input("How many threads do you want to use? (optional, leave empty for default setting [" + str(thread_default_count) + "])")

num = int(num)
if thread_num == "":
    thread_num = thread_default_count
else:
    thread_num = int(thread_num)

chunk_size = int(num / thread_num)

threads = []

t1 = time.clock()

for i in range(0, thread_num):
    thread = SumCalc(chunk_size * i, chunk_size * (i + 1))
    threads += [thread]
    thread.start()

for t in threads:
    t.join()

t2 = time.clock()

print(str(SumCalc.total))
print(str((t2 - t1) * 1000000) + " ms")
print(str(thread_num) + " thread(s)")
