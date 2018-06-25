import threading
import queue
import math

class Producer(threading.Thread):
    """
    Producer searches for prime numbers in a certain range and writes them into a queue.
    """
    def __init__(self, queue, start_num, end_num):
        """
        Initializes the super class and some variables

        :param queue: the queue
        :param start_num: the start number of the number range
        :param end_num: the end number of the number range
        """
        threading.Thread.__init__(self)
        self.queue = queue
        if start_num < 3:
            print("Start number can't be smaller than 3, starting from 3")
            self.start_num = 3      # starting from the smallest possible prime number
        else:
            self.start_num = start_num
        self.end_num = end_num

    def run(self):
        """
        Searches for prime numbers and writes them into a queue

        :return: None
        """
        count = self.start_num

        while True:
            is_prime = True
            for x in range(2, int(math.sqrt(count) + 1)):
                if count % x == 0:
                    is_prime = False
                    break
            if is_prime:
                self.queue.put(count)
                self.queue.join()
            if count >= self.end_num:
                break
            count += 1
        self.queue.join()
        self.queue.put("eof")      # tells the Consumer that no more numbers are coming


class Consumer(threading.Thread):
    """
    Reads numbers out of the queue, prints them in the console and writes them in a simple text file.
    """
    def __init__(self, queue, file):
        """
        Initializes the super class and some variables

        :param queue: the queue
        :param file: the writable text file
        """
        threading.Thread.__init__(self)
        self.queue = queue
        self.file = file

    def run(self):
        """
        Reads numbers out of a queue, prints them in the console and writes then in a simple text file.

        :return: None
        """
        while True:
            number = self.queue.get()
            if number == "eof":
                self.file.close()
                break
            print(str(number))
            self.file.write(str(number) + "\n")
            self.queue.task_done()


queue = queue.Queue()
file = open("prime.txt", "w")

start_num = int(input("start: "))
end_num = int(input("end: "))

producer = Producer(queue, start_num, end_num)
consumer = Consumer(queue, file)

producer.start()
consumer.start()

producer.join()
consumer.join()



